def printer_error(s):
    errors = sum(1 for char in s if char > 'm')
    return f'{errors}/{len(s)}'