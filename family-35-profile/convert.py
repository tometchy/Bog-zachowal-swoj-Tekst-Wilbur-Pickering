import re
import sys
import os

def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = [line.strip('\n') for line in f.readlines()]

    markers = []
    verses = []
    texts = []

    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        
        # Check if we are at the start of a markers block
        if re.match(r'^[+-]+$', line) or re.match(r'^[+-]+[0-9]+:[0-9]+', line):
            current_markers = []
            current_verses = []
            
            # Read markers and verses for this section (could be multiple pages)
            while i < len(lines):
                line = lines[i]
                if not line.strip():
                    i += 1
                    continue
                
                m_marker = re.match(r'^([+-]+)$', line)
                m_both = re.match(r'^([+-]+)([0-9]+:[0-9]+.*)$', line)
                m_verse = re.match(r'^([0-9]+:[0-9]+.*)$', line)
                
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
                        m_v = re.match(r'^([0-9]+:[0-9]+.*)$', line)
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
                        if re.match(r'^[+-]+$', next_line) or re.match(r'^[+-]+[0-9]+:[0-9]+', next_line):
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
            
            while i < len(lines) and len(collected_texts) < num_expected_texts:
                line = lines[i]
                if not line.strip():
                    i += 1
                    continue
                
                # Ignore isolated verse numbers that might be PDF artifacts
                if re.match(r'^[0-9]+:[0-9]+$', line.strip()):
                    # Check if this could be a real marker+verse start (not expected here)
                    # For now just skip it if we are expecting texts
                    i += 1
                    continue
                
                # If it's a marker block, we stopped early? 
                if re.match(r'^[+-]+$', line) or re.match(r'^[+-]+[0-9]+:[0-9]+', line):
                    break

                # It's a text line or continuation
                # A new text usually contains || or starts with greek/word
                # A continuation starts with [ or is short
                if ('||' in line or '[' in line or ']' in line or '%' in line) and not (line.strip().startswith('[') and collected_texts):
                    # Potential new text
                    # But wait, if it starts with '[', it might be a continuation!
                    # The rule: if we still need texts, and this line doesn't look like a continuation, it's a new text.
                    if line.strip().startswith('[') and collected_texts:
                        collected_texts[-1] = collected_texts[-1] + " " + line.strip()
                    else:
                        collected_texts.append(line.strip())
                else:
                    if collected_texts:
                        collected_texts[-1] = collected_texts[-1] + " " + line.strip()
                    else:
                        # First text in block
                        collected_texts.append(line.strip())
                i += 1
            
            texts.extend(collected_texts)
        else:
            i += 1

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
    
    for idx, row in enumerate(formatted_rows):
        if idx == 92:
            output_content += "\n"
            output_content += "|  |  |  |\n"
            output_content += "|:----|:--------|:-----------------------------------|\n"
        output_content += row + "\n"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output_content.rstrip('\n'))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py input.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = input_file.replace('.txt', '.md')
    process_file(input_file, output_file)
