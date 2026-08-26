Gotowe — wybrałem Python, bo pozwala jednocześnie renderować PDF, analizować fonty i wywołać model wizyjny.

Pliki:

* [pdf_page_to_markdown.py](sandbox:/workspace/scratch/2dd690abb72a/pickering-repo/pdf_page_to_markdown.py)
* [requirements-pdf-page.txt](sandbox:/workspace/scratch/2dd690abb72a/pickering-repo/requirements-pdf-page.txt)

Umieść je w głównym katalogu repozytorium, a następnie:

```bash
python3 -m venv .venv-pdf
.venv-pdf/bin/pip install -r requirements-pdf-page.txt
export OPENAI_API_KEY='TWÓJ_KLUCZ'
```

Klucz API tworzy się według [oficjalnego quickstartu OpenAI](https://developers.openai.com/api/docs/quickstart).

Uruchomienie dla jednostronicowego PDF-u:

```bash
.venv-pdf/bin/python pdf_page_to_markdown.py 119 --verify
```

Możesz podać również:

```bash
.venv-pdf/bin/python pdf_page_to_markdown.py 119.pdf --verify
.venv-pdf/bin/python pdf_page_to_markdown.py neway/119/119.pdf --verify
```

Powstaną:

```text
neway/119/119.jpg
neway/119/119.md
```

Dla pełnego `neway/plik.pdf`:

```bash
.venv-pdf/bin/python pdf_page_to_markdown.py plik.pdf --page 119 --verify
```

Najważniejsze opcje:

* `--verify` — drugi przebieg API, dokładnie kontrolujący grekę, `++--`, `||`, procenty i indeksy; oznacza dwa wywołania API.
* `--force` — nadpisuje istniejące wyniki.
* `--keep-page-number` — zachowuje numer strony.
* `--render-only` — generuje tylko JPG.
* `--model gpt-5.6-terra` — tańszy wariant; domyślnie jest dokładniejszy `gpt-5.6`.

Skrypt przesyła jednostronicowy PDF w `detail=high`, dzięki czemu model otrzymuje zarówno warstwę tekstową, jak i obraz strony — zgodnie z [dokumentacją wejść PDF](https://developers.openai.com/api/docs/guides/file-inputs). Dodatkowo dostaje współrzędne, fonty, pogrubienia i indeksy odczytane lokalnie.

Sprawdziłem lokalnie wszystkie 331 rozdzielonych PDF-ów oraz zgodność zależności z ARM64/Pythonem 3.13. Pusta strona `268.pdf` jest obsługiwana bez wywoływania API. Live API nie zostało wywołane, ponieważ środowisko nie ma Twojego klucza.
