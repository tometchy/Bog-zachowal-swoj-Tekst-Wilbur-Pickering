import re
import sys
import os

VERSE_PATTERN = (
    r'(?:'
    r'(?:[1-2]?[A-Za-z]+\.?)\s+(?:[0-9]+:[0-9]+(?:[a-zª]|,etc\.)?|[0-9]+)'
    r'|[0-9]+:[0-9]+(?:[a-zª])?'
    r')'
)


def split_pdf_line(line):
    """Split marker/verse/text fragments joined by PDF text extraction."""
    fragments = []
    remaining = line

    while remaining:
        marker_and_verse = re.match(
            rf'^([+-]+)({VERSE_PATTERN})', remaining
        )
        verse = re.match(rf'^({VERSE_PATTERN})', remaining)

        if marker_and_verse:
            fragments.extend(marker_and_verse.groups()[:2])
            remaining = remaining[marker_and_verse.end():]
        elif verse:
            tail = remaining[verse.end():]
            # A parenthetical cross-reference such as "2:17)" is text,
            # not a standalone Acts-style verse heading.
            if re.fullmatch(r'[0-9]+:[0-9]+(?:[a-zª])?', verse.group(1)) and tail.startswith(')'):
                fragments.append(remaining)
                break
            fragments.append(verse.group(1))
            remaining = tail
        else:
            fragments.append(remaining)
            break

    return fragments or ['']


def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = []
        for line in f:
            lines.extend(split_pdf_line(line.rstrip('\n')))

    markers = []
    verses = []
    texts = []
    detected_wraps = []
    column_errors = []

    def print_wrap_report():
        print(f"Wykryte złamania wierszy ({len(detected_wraps)}):")
        if detected_wraps:
            for verse, continuation in detected_wraps:
                print(f"  {verse}: {continuation}")
        else:
            print("  brak")

    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        
        # Check if we are at the start of a markers block
        if re.match(r'^[+-]+$', line) or re.match(rf'^[+-]+{VERSE_PATTERN}', line):
            current_markers = []
            current_verses = []
            
            # Read markers and verses for this section (could be multiple pages)
            while i < len(lines):
                line = lines[i]
                if not line.strip():
                    i += 1
                    continue
                
                m_marker = re.match(r'^([+-]+)$', line)
                m_both = re.match(rf'^([+-]+)({VERSE_PATTERN})$', line)
                m_verse = re.match(rf'^({VERSE_PATTERN})$', line)
                
                if m_marker:
                    current_markers.append(m_marker.group(1))
                    i += 1
                elif m_both:
                    current_markers.append(m_both.group(1))
                    current_verses.append(m_both.group(2))
                    i += 1
                    # Now we expect verses
                    while i < len(lines):
                        line = lines[i]
                        if not line.strip():
                            i += 1
                            continue
                        m_v = re.match(rf'^({VERSE_PATTERN})$', line)
                        if m_v:
                            current_verses.append(m_v.group(1))
                            i += 1
                            if len(current_verses) == len(current_markers):
                                break
                        else:
                            break
                elif m_verse:
                    # Should not happen before marker+verse, but handle just in case
                    current_verses.append(m_verse.group(1))
                    i += 1
                else:
                    break
                
                # Check if this sub-section is complete
                if len(current_markers) > 0 and len(current_markers) == len(current_verses):
                    # Check if next line is another markers block or start of texts
                    next_i = i
                    while next_i < len(lines) and not lines[next_i].strip():
                        next_i += 1
                    if next_i < len(lines):
                        next_line = lines[next_i]
                        if re.match(r'^[+-]+$', next_line) or re.match(rf'^[+-]+{VERSE_PATTERN}', next_line):
                            # More markers/verses coming in this block
                            i = next_i
                            continue
                        else:
                            # End of markers/verses block, texts follow
                            break
                    else:
                        break
            
            markers.extend(current_markers)
            verses.extend(current_verses)
            
            # Now read texts for these verses
            num_expected_texts = len(current_markers)
            collected_texts = []

            def append_continuation(continuation):
                verse_index = len(collected_texts) - 1
                verse = (current_verses[verse_index]
                         if 0 <= verse_index < len(current_verses)
                         else '?')
                collected_texts[-1] += " " + continuation.strip()
                detected_wraps.append((verse, continuation.strip()))
            
            while i < len(lines):
                line = lines[i]
                if not line.strip():
                    i += 1
                    continue

                # Reaching the expected number of readings does not
                # necessarily mean the final reading is complete: its PDF
                # line can still continue with "~ ..." or "[...%]".
                if len(collected_texts) >= num_expected_texts:
                    stripped = line.strip()
                    last_is_incomplete = collected_texts and '%' not in collected_texts[-1]
                    is_pipe_continuation = stripped.startswith('||')
                    is_parenthetical_continuation = (
                        stripped.startswith('(')
                        or re.match(r'^[0-9]+:[0-9]+\)', stripped)
                    )
                    if (not stripped.startswith(('[', '~'))
                            and not is_pipe_continuation
                            and not is_parenthetical_continuation
                            and not last_is_incomplete):
                        break
                
                # Ignore isolated verse numbers that might be PDF artifacts
                if re.fullmatch(VERSE_PATTERN, line.strip()):
                    # Check if this could be a real marker+verse start (not expected here)
                    # For now just skip it if we are expecting texts
                    i += 1
                    continue
                
                # If it's a marker block, we stopped early? 
                if re.match(r'^[+-]+$', line) or re.match(rf'^[+-]+{VERSE_PATTERN}', line):
                    break

                # It's a text line or continuation
                # A new text usually contains || or starts with greek/word.
                # Wrapped continuations in the source PDF can start with a
                # percentage ("[") or with a transposition marker ("~").
                stripped = line.strip()
                is_pipe_continuation = stripped.startswith('||')
                is_parenthetical_continuation = (
                    stripped.startswith('(')
                    or re.match(r'^[0-9]+:[0-9]+\)', stripped)
                )
                is_continuation = (
                    stripped.startswith(('[', '~'))
                    or is_pipe_continuation
                    or is_parenthetical_continuation
                ) and collected_texts
                if is_continuation:
                    append_continuation(line)
                elif '||' in line or '[' in line or ']' in line or '%' in line:
                    # Potential new text
                    collected_texts.append(line.strip())
                else:
                    # A long new reading may wrap before its percentage and
                    # therefore have no marker characters on its first line.
                    # If the preceding reading is already complete enough to
                    # contain a percentage, this plain line starts a new one.
                    if collected_texts and '%' in collected_texts[-1]:
                        collected_texts.append(line.strip())
                    elif collected_texts:
                        append_continuation(line)
                    else:
                        # First text in block
                        collected_texts.append(line.strip())
                i += 1
            
            texts.extend(collected_texts)
            block_counts = (
                len(current_markers),
                len(current_verses),
                len(collected_texts),
            )
            if len(set(block_counts)) != 1:
                first_verse = current_verses[0] if current_verses else '?'
                last_verse = current_verses[-1] if current_verses else '?'
                column_errors.append((first_verse, last_verse, block_counts))
        else:
            i += 1

    total_counts = (len(markers), len(verses), len(texts))
    if len(set(total_counts)) != 1 or column_errors:
        print_wrap_report()
        print("BŁĄD: liczba wierszy w kolumnach nie jest zgodna.", file=sys.stderr)
        print(
            f"  Łącznie: znaczniki={total_counts[0]}, "
            f"wersety={total_counts[1]}, teksty={total_counts[2]}",
            file=sys.stderr,
        )
        for first_verse, last_verse, counts in column_errors:
            print(
                f"  Blok {first_verse}–{last_verse}: znaczniki={counts[0]}, "
                f"wersety={counts[1]}, teksty={counts[2]}",
                file=sys.stderr,
            )
        raise ValueError("Niezgodna liczba wierszy w kolumnach")

    # Format the data
    formatted_rows = []
    for m, v, t in zip(markers, verses, texts):
        # Format verse
        v = v.replace('ª', 'a')
        v = re.sub(r'([0-9]+:[0-9]+)([a-z])', r'\1^\2^', v)
        
        # Format text
        t = re.sub(r'(\d+)(st|nd|rd|th)', r'\1^\2^', t)
        t = t.replace('f35pt', '**f^35pt^**')
        # Fix spaces around ||
        t = t.replace('||', ' || ')
        t = re.sub(r'\s+', ' ', t).strip()
        t = t.replace(' || ', ' || ') # keep it as is in MD
        
        # The MD output uses \|\| for escaped pipes in table
        t_md = t.replace('||', r'\|\|')
        
        formatted_rows.append(f"| {m} | {v} | {t_md} |")

    # Write to file
    output_content = "|  |  |  |\n"
    output_content += "|:----|:--------|:-----------------------------------|\n"
    
    for row in formatted_rows:
        output_content += row + "\n"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_content.rstrip('\n'))

    print_wrap_report()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py input.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = input_file.replace('.txt', '.md')
    try:
        process_file(input_file, output_file)
    except ValueError as error:
        print(f"Przerwano: {error}.", file=sys.stderr)
        sys.exit(1)
