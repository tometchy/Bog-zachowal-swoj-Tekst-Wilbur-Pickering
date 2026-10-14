-- A fenced div keeps dense apparatus tables readable without raw LaTeX tables.
-- Column proportions remain in the Markdown separator row for all writers.
function Div(div)
  if not div.classes:includes('compact-table') then
    return nil
  end
  if FORMAT:match('latex') then
    if div.classes:includes('natural-columns') then
      div = div:walk({Table = function(tbl)
        for _, column in ipairs(tbl.colspecs) do
          column[2] = nil
        end
        return tbl
      end})
    end
    local padding = div.classes:includes('natural-columns') and '3pt' or '2pt'
    div.content:insert(1, pandoc.RawBlock('latex',
      '\\begingroup\\footnotesize\\setlength{\\tabcolsep}{' .. padding .. '}'))
    div.content:insert(pandoc.RawBlock('latex', '\\endgroup'))
    return div.content
  elseif FORMAT == 'docx' then
    -- Table cells reset the surrounding paragraph style in the DOCX writer.
    -- Put the style on each cell paragraph, keeping native Word tables.
    local function compact_paragraph(block)
      return pandoc.Div({pandoc.Para(block.content)},
        {['custom-style'] = 'Compact Table'})
    end
    return div:walk({Plain = compact_paragraph, Para = compact_paragraph})
  end
end
