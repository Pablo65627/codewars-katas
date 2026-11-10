def remove_html_markup(s):
    tag = False
    out = ""

    for c in s:
        if c == '<':
            tag = True   # Start of markup
        elif c == '>':
            tag = False  # End of markup
        elif not tag:
            out = out + c

    return out

print remove_html_markup("<b>foo</b>")
