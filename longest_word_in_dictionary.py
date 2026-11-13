def find_longest(string, dictionary):
    def is_subsequence(word):
        i = 0

        for char in string:
            if i < len(word) and char == word[i]:
                i += 1

        return i == len(word)

    result = ""

    for word in dictionary:
        if is_subsequence(word):
            if len(word) > len(result):
                result = word
            elif len(word) == len(result) and word < result:
                result = word

    return result