def alphabet_position(text):

    import string
    
    alphabetPositions = ""
    for character in text.lower().replace(' ',''):
        if character not in (string.punctuation + string.digits):
            alphabetPositions = alphabetPositions + ' ' + str(string.ascii_lowercase.index(character) + 1)
    
    return alphabetPositions.strip()