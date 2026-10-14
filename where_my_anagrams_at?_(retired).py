def anagrams(word, words):
    target_sorted = sorted(word)
    
    return [w for w in words if sorted(w) == target_sorted] 