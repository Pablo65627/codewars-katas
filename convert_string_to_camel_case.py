import re

def to_camel_case(text):
    if not text:
        return ""
    
    words = re.split(r'[-_]', text)
    
    return words[0] + ''.join(word.capitalize() for word in words[1:])