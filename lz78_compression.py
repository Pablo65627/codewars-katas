import re

def encoder(data):
    dictionary = {'': 0}
    dict_size = 1
    output = []
    
    current_str = ""
    i = 0
    n = len(data)
    
    while i < n:
        current_str += data[i]
        
        if current_str not in dictionary:
            prefix = current_str[:-1]
            last_char = current_str[-1]
            
            output.append(f"{dictionary[prefix]}{last_char}")
            
            dictionary[current_str] = dict_size
            dict_size += 1
            
            current_str = ""
        
        i += 1
        
    if current_str:
        output.append(str(dictionary[current_str]))
        
    return "".join(output)

def decoder(data):
    dictionary = {0: ''}
    dict_size = 1
    output = []
    
    tokens = re.findall(r'(\d+)([A-Z]?)', data)
    
    for index_str, char in tokens:
        index = int(index_str)
        string_val = dictionary[index] + char
        output.append(string_val)
        
        dictionary[dict_size] = string_val
        dict_size += 1
        
    return "".join(output)