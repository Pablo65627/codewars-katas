import re

def increment_string(s):
    match = re.search(r'\d+$', s)

    if not match:
        return s + "1"

    number = match.group()
    incremented = str(int(number) + 1)

    # Preserve leading-zero width
    if len(incremented) < len(number):
        incremented = incremented.zfill(len(number))

    return s[:match.start()] + incremented