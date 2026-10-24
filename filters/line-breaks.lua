-- Keep HTML line breaks in pipe-table cells in every Pandoc output format.
-- Raw HTML is otherwise omitted by the LaTeX and DOCX writers.
function RawInline(inline)
  if inline.format == 'html' and inline.text:lower():match('^<br%s*/?>$') then
    return pandoc.LineBreak()
  end
end
