#!/usr/bin/env python3
"""Create a local JPG rendering and a font-aware Markdown transcription.

The script is tailored to the PDFs in ``neway`` but also accepts an arbitrary
text-based PDF. It never calls an API or any other network endpoint:

* PyMuPDF renders the selected page and exposes its text spans, fonts and
  coordinates.
* PyMuPDF4LLM's local layout model handles ordinary prose and ruled tables.
* A deterministic coordinate parser handles the dense, unruled apparatus
  tables used in this book, because general layout models tend to merge rows.

Examples (run from the repository root):

    python3 pdf_page_to_markdown_local.py 119
    python3 pdf_page_to_markdown_local.py 119.pdf
    python3 pdf_page_to_markdown_local.py neway/119/119.pdf
    python3 pdf_page_to_markdown_local.py neway/plik.pdf --page 119

By default the output is written next to the PDF (``119.jpg`` and ``119.md``).
"""

from __future__ import annotations

import argparse
import os
import re
import statistics
import sys
import unicodedata
from collections import Counter
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# The local layout wheel uses ONNX Runtime. Official ONNX Runtime binaries
# enable telemetry by default on Linux, so disable it before that module can be
# imported. This makes the no-network guarantee explicit, including telemetry.
os.environ.setdefault("ORT_DISABLE_TELEMETRY", "1")

try:
    import pymupdf
except ImportError as error:  # pragma: no cover - exercised on a clean machine
    raise SystemExit(
        "Brakuje PyMuPDF. Utworz srodowisko i zainstaluj zaleznosci:\n"
        "  python3 -m venv .venv-pdf\n"
        "  .venv-pdf/bin/pip install -r requirements-pdf-page-local.txt"
    ) from error


# These are the SymbolMT glyphs that actually occur in all PDFs under neway/.
# Their source font has no useful ToUnicode map, so MuPDF returns characters
# from Unicode's Private Use Area.
SYMBOL_MT_MAP = str.maketrans(
    {
        "\uf020": " ",
        "\uf07e": "~",
        "\uf0b1": "±",
        "\uf0b7": "•",
        "\uf0b8": "÷",
        "\uf0c0": "ℵ",
    }
)

# Page 119 contains one word in the legacy Bwgrkl font without a ToUnicode
# map. The mapping is kept complete enough for other basic Greek text too.
BWGRK_LOWER_MAP = str.maketrans(
    {
        "a": "α",
        "b": "β",
        "g": "γ",
        "d": "δ",
        "e": "ε",
        "z": "ζ",
        "h": "η",
        "q": "θ",
        "i": "ι",
        "k": "κ",
        "l": "λ",
        "m": "μ",
        "n": "ν",
        "c": "ξ",
        "o": "ο",
        "p": "π",
        "r": "ρ",
        "s": "σ",
        "t": "τ",
        "u": "υ",
        "f": "φ",
        "x": "χ",
        "y": "ψ",
        "w": "ω",
    }
)

PROFILE_MARKER_RE = re.compile(r"^[+-]+$")
VERSE_RE = re.compile(
    r"^(?:(?:[1-3]\s*)?[A-Za-z]+\.?\s+)?"
    r"\d+:\d+(?:[a-zª])?$",
    flags=re.IGNORECASE,
)
TRAILING_PAGE_NUMBER_RE = re.compile(r"^\d+$")
FOOTNOTE_ID_RE = re.compile(r"^\d{1,2}$")


@dataclass(frozen=True)
class PdfLine:
    """One line object from a MuPDF text block."""

    x0: float
    y0: float
    baseline: float
    spans: tuple[dict[str, Any], ...]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Lokalnie tworzy JPG wybranej strony PDF i transkrypcje Markdown "
            "z zachowaniem pogrubien, kursywy, indeksow oraz tabel."
        )
    )
    parser.add_argument(
        "pdf",
        help="sciezka do PDF-u, sama nazwa (119.pdf) albo sam numer (119)",
    )
    parser.add_argument(
        "--page",
        type=int,
        help="numer strony od 1; wymagany tylko dla wielostronicowego PDF-u",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        help="katalog wynikowy; domyslnie katalog PDF-u",
    )
    parser.add_argument(
        "--dpi", type=int, default=300, help="DPI pliku JPG (domyslnie 300)"
    )
    parser.add_argument(
        "--jpeg-quality",
        type=int,
        default=95,
        help="jakosc JPG 1-100 (domyslnie 95)",
    )
    parser.add_argument(
        "--engine",
        choices=("hybrid", "layout", "spans"),
        default="hybrid",
        help=(
            "hybrid: najlepszy wariant dla tego katalogu (domyslnie); "
            "layout: zawsze lokalny model ukladu; spans: tylko deterministyczny "
            "odczyt fontow i wspolrzednych"
        ),
    )
    parser.add_argument(
        "--keep-page-number",
        action="store_true",
        help="zachowaj samodzielny numer strony u dolu/gory",
    )
    parser.add_argument(
        "--render-only",
        action="store_true",
        help="utworz tylko JPG, bez pliku Markdown",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="nadpisz istniejace pliki wynikowe",
    )
    args = parser.parse_args()

    if args.page is not None and args.page < 1:
        parser.error("--page musi byc liczba >= 1")
    if args.dpi < 72 or args.dpi > 1200:
        parser.error("--dpi musi miescic sie w zakresie 72-1200")
    if not 1 <= args.jpeg_quality <= 100:
        parser.error("--jpeg-quality musi miescic sie w zakresie 1-100")
    return args


def resolve_pdf(raw_value: str) -> Path:
    """Resolve a direct path or a convenient ``neway/<n>/<n>.pdf`` shorthand."""

    supplied = Path(raw_value).expanduser()
    candidates: list[Path] = [supplied]

    name = supplied.name
    if supplied.suffix.lower() != ".pdf":
        name = f"{name}.pdf"
        candidates.append(supplied.with_suffix(".pdf"))

    stem = Path(name).stem
    roots = (Path.cwd(), Path(__file__).resolve().parent)
    for root in roots:
        candidates.extend(
            (
                root / name,
                root / "neway" / name,
                root / "neway" / stem / name,
            )
        )

    seen: set[Path] = set()
    for candidate in candidates:
        candidate = candidate.resolve()
        if candidate in seen:
            continue
        seen.add(candidate)
        if candidate.is_file():
            if candidate.suffix.lower() != ".pdf":
                raise SystemExit(f"To nie jest PDF: {candidate}")
            return candidate

    tried = "\n  ".join(str(path) for path in seen)
    raise SystemExit(f"Nie znaleziono PDF-u. Sprawdzone sciezki:\n  {tried}")


def save_jpeg(page: pymupdf.Page, destination: Path, dpi: int, quality: int) -> None:
    temporary = destination.with_name(f".{destination.name}.{os.getpid()}.tmp.jpg")
    try:
        pixmap = page.get_pixmap(dpi=dpi, colorspace=pymupdf.csRGB, alpha=False)
        pixmap.save(str(temporary), output="jpeg", jpg_quality=quality)
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)


def atomic_write_text(destination: Path, content: str) -> None:
    temporary = destination.with_name(f".{destination.name}.{os.getpid()}.tmp")
    try:
        temporary.write_text(content, encoding="utf-8")
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)


def page_is_visually_blank(page: pymupdf.Page) -> bool:
    return (
        not page.get_text().strip()
        and not page.get_images(full=True)
        and not page.get_drawings()
    )


def decode_pdf_text(text: str, font: str = "") -> str:
    """Repair the known broken font encodings without changing source wording."""

    if font.startswith("Bwgrk"):
        text = text.translate(BWGRK_LOWER_MAP)
    text = text.translate(SYMBOL_MT_MAP)

    # The source uses an RTL Hebrew glyph as a visual substitute for the
    # mathematical manuscript siglum. MuPDF reverses a preceding parenthesis.
    text = text.replace("א)", "ℵ)").replace("א", "ℵ")
    text = text.replace(")ℵ)", "(ℵ)")
    text = text.replace("\u200b", "").replace("\u00ad", "")
    return unicodedata.normalize("NFC", text)


def line_from_dict(line: dict[str, Any]) -> PdfLine:
    spans = tuple(line.get("spans", ()))
    bbox = line.get("bbox", (0.0, 0.0, 0.0, 0.0))
    baselines = [
        float(span.get("origin", (0.0, bbox[1]))[1])
        for span in spans
        if str(span.get("text", "")).strip()
    ]
    baseline = max(baselines, default=float(bbox[1]))
    return PdfLine(float(bbox[0]), float(bbox[1]), baseline, spans)


def block_lines(block: dict[str, Any]) -> list[PdfLine]:
    return [line_from_dict(line) for line in block.get("lines", ())]


def plain_spans(spans: Iterable[dict[str, Any]]) -> str:
    return "".join(
        decode_pdf_text(str(span.get("text", "")), str(span.get("font", "")))
        for span in spans
    )


def plain_line(line: PdfLine) -> str:
    return re.sub(r"\s+", " ", plain_spans(line.spans)).strip()


def plain_block(block: dict[str, Any]) -> str:
    return " ".join(filter(None, (plain_line(line) for line in block_lines(block))))


def body_font_size(blocks: Sequence[dict[str, Any]]) -> float:
    scores: Counter[float] = Counter()
    for block in blocks:
        for line in block.get("lines", ()):
            for span in line.get("spans", ()):
                text = decode_pdf_text(
                    str(span.get("text", "")), str(span.get("font", ""))
                ).strip()
                if not text:
                    continue
                size = round(float(span.get("size", 0.0)) * 2) / 2
                if size >= 7:
                    scores[size] += max(1, len(text))
    return scores.most_common(1)[0][0] if scores else 10.0


def group_by_baseline(
    lines: Iterable[PdfLine], tolerance: float = 1.25
) -> list[list[PdfLine]]:
    groups: list[list[PdfLine]] = []
    centers: list[float] = []
    visible_lines = (line for line in lines if plain_line(line))
    for line in sorted(visible_lines, key=lambda item: (item.baseline, item.x0)):
        if groups and abs(line.baseline - centers[-1]) <= tolerance:
            groups[-1].append(line)
            centers[-1] = statistics.fmean(item.baseline for item in groups[-1])
        else:
            groups.append([line])
            centers.append(line.baseline)
    for group in groups:
        group.sort(key=lambda item: item.x0)
    return groups


def is_superscript(
    span: dict[str, Any], normal_size: float, normal_baseline: float
) -> bool:
    flags = int(span.get("flags", 0))
    size = float(span.get("size", normal_size))
    baseline = float(span.get("origin", (0.0, normal_baseline))[1])
    return bool(flags & pymupdf.TEXT_FONT_SUPERSCRIPT) or (
        size <= normal_size * 0.78 and baseline < normal_baseline - normal_size * 0.12
    )


def is_subscript(
    span: dict[str, Any], normal_size: float, normal_baseline: float
) -> bool:
    size = float(span.get("size", normal_size))
    baseline = float(span.get("origin", (0.0, normal_baseline))[1])
    return (
        size <= normal_size * 0.78 and baseline > normal_baseline + normal_size * 0.12
    )


def wrap_style(core: str, bold: bool, italic: bool) -> str:
    if bold and italic:
        return f"***{core}***"
    if bold:
        return f"**{core}**"
    if italic:
        return f"*{core}*"
    return core


def normalize_inline_markdown(text: str) -> str:
    """Merge adjacent base/superscript style runs into valid Pandoc Markdown."""

    text = text.replace(")ℵ)", "(ℵ)")
    previous = None
    while previous != text:
        previous = text
        text = re.sub(
            r"\*\*([^*\n]+)\*\*\s*\*\*\^([^\^\n]+)\^\*\*",
            r"**\1^\2^**",
            text,
        )
        text = re.sub(
            r"\*\*([^*\n]+)\*\*\s*\^([^\^\n]+)\^",
            r"**\1^\2^**",
            text,
        )
        text = re.sub(
            r"\*([^*\n]+)\*\s*\*\^([^\^\n]+)\^\*",
            r"*\1^\2^*",
            text,
        )
    text = re.sub(r"(?<=\d)ª\b", "^a^", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" +([,.;:!\)])", r"\1", text)
    text = re.sub(r" +\?(?=\s|$)", "?", text)
    text = re.sub(r"([\(\[]) +", r"\1", text)
    text = re.sub(r"\*([^*\n]+)\*\s+\*([^*\n]+)\*", r"*\1 \2*", text)
    return text.strip()


def format_spans(
    spans: Sequence[dict[str, Any]], footnote_ids: set[str] | None = None
) -> str:
    if not spans:
        return ""

    visible = [span for span in spans if str(span.get("text", "")).strip()]
    if not visible:
        return ""
    normal_size = max(float(span.get("size", 0.0)) for span in visible)
    normal_baselines = [
        float(span.get("origin", (0.0, 0.0))[1])
        for span in visible
        if float(span.get("size", 0.0)) >= normal_size * 0.9
    ]
    normal_baseline = statistics.median(normal_baselines) if normal_baselines else 0.0

    pieces: list[str] = []
    for span in spans:
        raw = decode_pdf_text(str(span.get("text", "")), str(span.get("font", "")))
        if not raw:
            continue
        leading = raw[: len(raw) - len(raw.lstrip())]
        trailing = raw[len(raw.rstrip()) :]
        core = raw.strip()
        if not core:
            pieces.append(" ")
            continue

        flags = int(span.get("flags", 0))
        bold = bool(flags & pymupdf.TEXT_FONT_BOLD)
        italic = bool(flags & pymupdf.TEXT_FONT_ITALIC)
        superscript = is_superscript(span, normal_size, normal_baseline)
        subscript = is_subscript(span, normal_size, normal_baseline)

        if superscript and footnote_ids and core in footnote_ids:
            styled = f"[^{core}]"
        else:
            if superscript:
                core = f"^{core}^"
            elif subscript:
                core = f"~{core}~"
            styled = wrap_style(core, bold, italic)
        pieces.append((" " if leading else "") + styled + (" " if trailing else ""))

    return normalize_inline_markdown("".join(pieces))


def join_wrapped_lines(lines: Sequence[str]) -> str:
    result = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if not result:
            result = line
            continue

        plain_start = re.sub(r"^[*_`]+", "", line)
        starts_lower = bool(plain_start and plain_start[0].islower())
        if result.endswith("-") and starts_lower:
            result = result[:-1] + line
        else:
            result += " " + line
    return normalize_inline_markdown(result)


def block_is_profile(block: dict[str, Any]) -> bool:
    matches = 0
    for group in group_by_baseline(block_lines(block)):
        cells = [(plain_line(line), line.x0) for line in group if plain_line(line)]
        if len(cells) < 2:
            continue
        if PROFILE_MARKER_RE.fullmatch(cells[0][0]) and VERSE_RE.fullmatch(cells[1][0]):
            matches += 1
    return matches >= 3


def block_is_dense_grid(block: dict[str, Any]) -> bool:
    groups = group_by_baseline(block_lines(block))
    if len(groups) < 5:
        return False
    multi = 0
    for group in groups:
        nonempty = [line for line in group if plain_line(line)]
        if len(nonempty) >= 2 and nonempty[-1].x0 - nonempty[0].x0 >= 18:
            multi += 1
    return multi >= 4 and multi >= len(groups) * 0.4


def escape_table_cell(text: str) -> str:
    return text.replace("|", r"\|").strip()


def table_markdown(rows: Sequence[Sequence[str]], columns: int) -> str:
    if not rows:
        return ""
    header = "| " + " | ".join("" for _ in range(columns)) + " |"
    separator = "|" + "|".join("---" for _ in range(columns)) + "|"
    body = [
        "| " + " | ".join(escape_table_cell(cell) for cell in row) + " |"
        for row in rows
    ]
    return "\n".join((header, separator, *body))


def format_profile_block(block: dict[str, Any], footnote_ids: set[str]) -> str:
    rows: list[list[str]] = []
    preamble: list[str] = []

    for group in group_by_baseline(block_lines(block)):
        nonempty = [line for line in group if plain_line(line)]
        if not nonempty:
            continue
        texts = [plain_line(line) for line in nonempty]
        is_row = (
            len(nonempty) >= 2
            and PROFILE_MARKER_RE.fullmatch(texts[0])
            and VERSE_RE.fullmatch(texts[1])
        )
        if is_row:
            marker = texts[0]
            verse = format_spans(nonempty[1].spans, footnote_ids)
            reading = " ".join(
                format_spans(line.spans, footnote_ids) for line in nonempty[2:]
            ).strip()
            rows.append([marker, verse, reading])
        elif rows:
            continuation = " ".join(
                format_spans(line.spans, footnote_ids) for line in nonempty
            ).strip()
            if continuation:
                rows[-1][2] = join_wrapped_lines((rows[-1][2], continuation))
        else:
            preamble.append(
                join_wrapped_lines(
                    [format_spans(line.spans, footnote_ids) for line in nonempty]
                )
            )

    parts: list[str] = []
    if preamble:
        title = join_wrapped_lines(preamble)
        parts.append(f"## {title}" if len(title) < 80 else title)
    table = table_markdown(rows, 3)
    if table:
        parts.append(table)
    return "\n\n".join(parts)


def cluster_x_positions(
    lines: Sequence[PdfLine], tolerance: float = 5.0
) -> list[float]:
    clusters: list[list[float]] = []
    for x in sorted(line.x0 for line in lines):
        if clusters and abs(x - statistics.fmean(clusters[-1])) <= tolerance:
            clusters[-1].append(x)
        else:
            clusters.append([x])
    recurring = [
        statistics.median(cluster) for cluster in clusters if len(cluster) >= 2
    ]
    return recurring[:8]


def nearest_column(x: float, columns: Sequence[float]) -> int:
    return min(range(len(columns)), key=lambda index: abs(columns[index] - x))


def format_grid_block(block: dict[str, Any], footnote_ids: set[str]) -> str:
    lines = block_lines(block)
    columns = cluster_x_positions(lines)
    if len(columns) < 2:
        return format_text_block(block, 10.0, footnote_ids)

    row_groups: list[list[str]] = []
    preamble: list[str] = []
    for group in group_by_baseline(lines):
        cells = ["" for _ in columns]
        assigned = False
        for line in group:
            text = format_spans(line.spans, footnote_ids)
            if not text:
                continue
            column = nearest_column(line.x0, columns)
            # A centered title that is far from every recurrent column is not
            # a cell; retain it above the table.
            if abs(columns[column] - line.x0) > 16 and not row_groups:
                preamble.append(text)
                continue
            cells[column] = join_wrapped_lines((cells[column], text))
            assigned = True
        if not assigned:
            if row_groups and any(any(cell for cell in row) for row in row_groups):
                row_groups.append(["" for _ in columns])
            continue

        if not cells[0] and row_groups and any(cells[1:]):
            previous = row_groups[-1]
            for index, cell in enumerate(cells):
                if cell:
                    previous[index] = join_wrapped_lines((previous[index], cell))
        else:
            row_groups.append(cells)

    tables: list[str] = []
    current: list[list[str]] = []
    for row in row_groups:
        if any(row):
            current.append(row)
        elif current:
            tables.append(table_markdown(current, len(columns)))
            current = []
    if current:
        tables.append(table_markdown(current, len(columns)))

    parts: list[str] = []
    if preamble:
        title = join_wrapped_lines(preamble)
        parts.append(f"## {title}" if len(title) < 80 else title)
    parts.extend(table for table in tables if table)
    return "\n\n".join(parts)


def extract_footnotes(
    blocks: Sequence[dict[str, Any]], page_height: float, body_size: float
) -> tuple[dict[str, str], set[int]]:
    notes: dict[str, list[str]] = {}
    note_block_indexes: set[int] = set()

    for index, block in enumerate(blocks):
        bbox = block.get("bbox", (0.0, 0.0, 0.0, 0.0))
        if float(bbox[1]) < page_height * 0.68:
            continue
        current: str | None = None
        found_marker = False
        for line_dict in block.get("lines", ()):
            spans = [
                span
                for span in line_dict.get("spans", ())
                if decode_pdf_text(
                    str(span.get("text", "")), str(span.get("font", ""))
                ).strip()
            ]
            if not spans:
                continue
            first_text = decode_pdf_text(
                str(spans[0].get("text", "")), str(spans[0].get("font", ""))
            ).strip()
            first_size = float(spans[0].get("size", body_size))
            line_max_size = max(float(span.get("size", body_size)) for span in spans)
            marker = (
                first_text
                if FOOTNOTE_ID_RE.fullmatch(first_text)
                and first_size <= line_max_size * 0.75
                else None
            )
            content_spans = spans
            if marker:
                current = marker
                notes.setdefault(current, [])
                content_spans = spans[1:]
                found_marker = True
            if current is not None and content_spans:
                notes[current].append(format_spans(content_spans, set()))
        if found_marker:
            note_block_indexes.add(index)

    joined = {
        number: join_wrapped_lines(lines)
        for number, lines in notes.items()
        if join_wrapped_lines(lines)
    }
    return joined, note_block_indexes


def is_page_number_block(
    block: dict[str, Any], page_height: float, keep_page_number: bool
) -> bool:
    if keep_page_number:
        return False
    text = plain_block(block).strip()
    bbox = block.get("bbox", (0.0, 0.0, 0.0, 0.0))
    return bool(
        TRAILING_PAGE_NUMBER_RE.fullmatch(text) and float(bbox[1]) >= page_height * 0.88
    )


def format_text_block(
    block: dict[str, Any], body_size: float, footnote_ids: set[str]
) -> str:
    lines = block_lines(block)
    formatted_lines = [format_spans(line.spans, footnote_ids) for line in lines]
    formatted_lines = [line for line in formatted_lines if line]
    if not formatted_lines:
        return ""

    # MuPDF represents a bullet and its text as two line objects on one
    # baseline. Keep it as a real Markdown list item.
    plain = [plain_line(line) for line in lines if plain_line(line)]
    if plain and plain[0] in {"•", "·"}:
        return "- " + join_wrapped_lines(formatted_lines[1:])

    content = join_wrapped_lines(formatted_lines)
    spans = [
        span
        for line in lines
        for span in line.spans
        if str(span.get("text", "")).strip()
    ]
    if not spans:
        return content
    max_size = max(float(span.get("size", 0.0)) for span in spans)
    short = len(re.sub(r"[*_^~]", "", content)) <= 90
    centered = float(block.get("bbox", (0.0, 0.0, 0.0, 0.0))[0]) >= 55
    all_italic = all(
        int(span.get("flags", 0)) & pymupdf.TEXT_FONT_ITALIC for span in spans
    )
    if short and (max_size >= body_size * 1.18 or (centered and all_italic)):
        return f"## {content}"
    return content


def append_footnotes(markdown: str, footnotes: dict[str, str]) -> str:
    if not footnotes:
        return markdown
    definitions = [f"[^{number}]: {text}" for number, text in footnotes.items()]
    return markdown.rstrip() + "\n\n" + "\n\n".join(definitions)


def raw_page_markdown(page: pymupdf.Page, keep_page_number: bool) -> tuple[str, str]:
    page_dict = page.get_text("dict", flags=pymupdf.TEXTFLAGS_DICT, sort=False)
    indexed_blocks = [
        (index, block)
        for index, block in enumerate(page_dict.get("blocks", ()))
        if int(block.get("type", 0)) == 0
    ]
    indexed_blocks.sort(
        key=lambda item: (
            round(float(item[1].get("bbox", (0, 0, 0, 0))[1]), 1),
            float(item[1].get("bbox", (0, 0, 0, 0))[0]),
        )
    )
    blocks = [block for _, block in indexed_blocks]
    size = body_font_size(blocks)
    footnotes, footnote_indexes = extract_footnotes(blocks, page.rect.height, size)
    footnote_ids = set(footnotes)

    parts: list[str] = []
    for index, block in enumerate(blocks):
        if index in footnote_indexes:
            continue
        if is_page_number_block(block, page.rect.height, keep_page_number):
            continue
        if not plain_block(block):
            continue
        if block_is_profile(block):
            rendered = format_profile_block(block, footnote_ids)
        elif block_is_dense_grid(block):
            rendered = format_grid_block(block, footnote_ids)
        else:
            rendered = format_text_block(block, size, footnote_ids)
        if rendered:
            parts.append(rendered)

    markdown = "\n\n".join(parts)
    markdown = append_footnotes(markdown, footnotes)
    return finalize_markdown(markdown), "spans"


def remove_layout_footnotes(markdown: str, footnotes: dict[str, str]) -> str:
    if not footnotes:
        return markdown
    # The layout engine emits bottom notes as block quotes. They are replaced
    # below by exact, font-aware Pandoc footnotes extracted from the PDF spans.
    lines = markdown.splitlines()
    result: list[str] = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("> ") and any(
            re.match(rf">\s*{re.escape(number)}(?:\s|$)", stripped)
            for number in footnotes
        ):
            continue
        result.append(line)
    return "\n".join(result)


def convert_html_scripts(text: str) -> str:
    # First merge identically styled bases and superscripts so that
    # **K**<sup>**r**</sup> becomes the requested **K^r^**.
    def merge_bold_superscript(match: re.Match[str]) -> str:
        base = match.group(1)
        script = re.sub(r"\*\*|__|(?<!\w)_(?!\s)|(?<!\s)_(?!\w)", "", match.group(2))
        return f"**{base}^{script.strip()}^**"

    text = re.sub(
        r"\*\*([^*\n]+)\*\*\s*<sup>([^\n]*?)</sup>",
        merge_bold_superscript,
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\*\*([^*\n]+)\*\*\s*<sup>\s*\*\*([^*\n]+)\*\*\s*</sup>",
        r"**\1^\2^**",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"_([^_\n]+)_\s*<sup>\s*_([^_\n]+)_\s*</sup>",
        r"*\1^\2^*",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"<sup>\s*\*\*([^*\n]+)\*\*\s*</sup>",
        r"^\1^",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"<sup>\s*_([^_\n]+)_\s*</sup>",
        r"^\1^",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"<sup>([^\n]*?)</sup>", r"^\1^", text, flags=re.IGNORECASE)
    text = re.sub(r"<sub>([^\n]*?)</sub>", r"~\1~", text, flags=re.IGNORECASE)
    return text


def space_around_bold_runs(text: str) -> str:
    """Repair spaces dropped by the layout engine around complete bold runs."""

    text = re.sub(r"(?<!\*)\*\*\*\*(?!\*)", "** **", text)
    output_lines: list[str] = []
    marker_re = re.compile(r"(?<!\*)\*\*(?!\*)")
    for line in text.splitlines():
        markers = list(marker_re.finditer(line))
        if len(markers) % 2:
            output_lines.append(line)
            continue
        rebuilt: list[str] = []
        cursor = 0
        for index, marker in enumerate(markers):
            chunk = line[cursor : marker.start()]
            opening = index % 2 == 0
            if opening:
                next_character = line[marker.end() : marker.end() + 1]
                if (
                    chunk
                    and (chunk[-1].isalnum() or chunk[-1] in ")]")
                    and next_character
                    and next_character.isalnum()
                ):
                    chunk += " "
            rebuilt.append(chunk)
            rebuilt.append("**")
            cursor = marker.end()
            if not opening:
                next_character = line[cursor : cursor + 1]
                if next_character and (
                    next_character.isalpha() or next_character in "ℵ["
                ):
                    rebuilt.append(" ")
        rebuilt.append(line[cursor:])
        output_lines.append("".join(rebuilt))
    return "\n".join(output_lines)


def finalize_markdown(markdown: str) -> str:
    markdown = decode_pdf_text(markdown)
    markdown = convert_html_scripts(markdown)
    markdown = markdown.replace("\r\n", "\n").replace("\r", "\n")
    markdown = re.sub(r"(?<=\d)ª\b", "^a^", markdown)
    markdown = re.sub(r"(?<![\w^])f35(pt)?\b", r"f^35\1^", markdown)
    markdown = re.sub(r"(?<!\w)_([^_\n]+)_(?!\w)", r"*\1*", markdown)
    markdown = re.sub(r"^\s*•\s+", "- ", markdown, flags=re.MULTILINE)
    markdown = re.sub(r"\(\s+([*_])", r"(\1", markdown)
    markdown = re.sub(r"([*_])\s+\)", r"\1)", markdown)
    markdown = re.sub(r"([*_]{1,3})\s+([,.;:!?])", r"\1\2", markdown)
    markdown = re.sub(r" +([,.;:!?])", r"\1", markdown)
    markdown = space_around_bold_runs(markdown)
    markdown = re.sub(r"(?<=\^)(?=ℵ)", " ", markdown)
    markdown = re.sub(r"(?<=ℵ)(?=\[)", " ", markdown)
    markdown = re.sub(r"(?<![.!?:;\n])[ \t]*\n[ \t]*\n(?=[a-zα-ω])", " ", markdown)
    markdown = re.sub(r"[ \t]+\n", "\n", markdown)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    markdown = unicodedata.normalize("NFC", markdown).strip()
    return markdown + ("\n" if markdown else "")


def layout_page_markdown(
    page: pymupdf.Page,
    source: Path,
    page_index: int,
    keep_page_number: bool,
) -> tuple[str, str]:
    try:
        import pymupdf4llm
    except ImportError as error:  # pragma: no cover - clean machine path
        raise SystemExit(
            "Brakuje PyMuPDF4LLM. Zainstaluj lokalne zaleznosci:\n"
            "  python3 -m venv .venv-pdf\n"
            "  .venv-pdf/bin/pip install -r requirements-pdf-page-local.txt"
        ) from error

    page_dict = page.get_text("dict", flags=pymupdf.TEXTFLAGS_DICT, sort=False)
    blocks = [
        block for block in page_dict.get("blocks", ()) if int(block.get("type", 0)) == 0
    ]
    size = body_font_size(blocks)
    footnotes, _ = extract_footnotes(blocks, page.rect.height, size)

    markdown = pymupdf4llm.to_markdown(
        source,
        pages=[page_index],
        use_ocr=False,
        force_text=True,
        header=keep_page_number,
        footer=keep_page_number,
        show_progress=False,
        page_separators=False,
        write_images=False,
        embed_images=False,
    )
    markdown = remove_layout_footnotes(str(markdown), footnotes)
    markdown = convert_html_scripts(markdown)

    for number in footnotes:
        markdown = re.sub(
            rf"(?<!\^)\^{re.escape(number)}\^(?!\^)", f"[^{number}]", markdown
        )
    markdown = append_footnotes(markdown, footnotes)
    return finalize_markdown(markdown), "layout"


def choose_hybrid_engine(page: pymupdf.Page) -> str:
    page_dict = page.get_text("dict", flags=pymupdf.TEXTFLAGS_DICT, sort=False)
    blocks = [
        block for block in page_dict.get("blocks", ()) if int(block.get("type", 0)) == 0
    ]
    if any(block_is_profile(block) or block_is_dense_grid(block) for block in blocks):
        return "spans"
    return "layout"


def markdown_for_page(
    page: pymupdf.Page,
    source: Path,
    page_index: int,
    engine: str,
    keep_page_number: bool,
) -> tuple[str, str]:
    selected = choose_hybrid_engine(page) if engine == "hybrid" else engine
    if selected == "spans":
        return raw_page_markdown(page, keep_page_number)
    return layout_page_markdown(
        page, source, page_index, keep_page_number=keep_page_number
    )


def main() -> int:
    args = parse_args()
    pdf_path = resolve_pdf(args.pdf)
    output_dir = (args.output_dir or pdf_path.parent).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        document = pymupdf.open(pdf_path)
    except Exception as error:
        raise SystemExit(f"Nie mozna otworzyc PDF-u {pdf_path}: {error}") from error

    with document:
        if document.page_count < 1:
            raise SystemExit(f"PDF nie ma stron: {pdf_path}")
        if document.page_count > 1 and args.page is None:
            raise SystemExit(
                f"PDF ma {document.page_count} stron. Podaj jedna z nich, np. --page 1."
            )

        page_number = args.page or 1
        if page_number > document.page_count:
            raise SystemExit(
                f"PDF ma tylko {document.page_count} stron, a podano --page {page_number}."
            )
        page_index = page_number - 1
        page = document[page_index]

        basename = pdf_path.stem
        if document.page_count > 1:
            basename += f"-page-{page_number:03d}"
        jpg_path = output_dir / f"{basename}.jpg"
        md_path = output_dir / f"{basename}.md"

        expected_outputs = [jpg_path] if args.render_only else [jpg_path, md_path]
        existing = [path for path in expected_outputs if path.exists()]
        if existing and not args.force:
            rendered = "\n  ".join(str(path) for path in existing)
            raise SystemExit(
                "Pliki wynikowe juz istnieja (uzyj --force, aby je nadpisac):\n  "
                + rendered
            )

        save_jpeg(page, jpg_path, args.dpi, args.jpeg_quality)
        print(f"JPG: {jpg_path}")
        if args.render_only:
            return 0

        if page_is_visually_blank(page):
            atomic_write_text(md_path, "")
            print(f"Markdown (pusta strona): {md_path}")
            return 0

        try:
            markdown, used_engine = markdown_for_page(
                page,
                pdf_path,
                page_index,
                engine=args.engine,
                keep_page_number=args.keep_page_number,
            )
        except Exception as error:
            raise SystemExit(
                f"Nie udalo sie lokalnie wygenerowac Markdownu: {error}\n"
                f"JPG pozostal zapisany: {jpg_path}"
            ) from error

        atomic_write_text(md_path, markdown)
        print(f"Markdown ({used_engine}, bez API): {md_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\nPrzerwano.", file=sys.stderr)
        raise SystemExit(130)
