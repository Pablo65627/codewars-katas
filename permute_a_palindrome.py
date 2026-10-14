from collections import Counter

def permute_a_palindrome(texto):
    frecuencias = Counter(texto)
    
    impares = sum(1 for cantidad in frecuencias.values() if cantidad % 2 != 0)
    
    return impares <= 1
