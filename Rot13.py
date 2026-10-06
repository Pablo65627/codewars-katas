def rot13(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':  
            result += chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':  
            result += chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
        else:
            result += char 
    return result
