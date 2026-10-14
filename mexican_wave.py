def wave(people):
    result = []

    for i, char in enumerate(people):
        if char == " ":
            continue
        result.append(people[:i] + char.upper() + people[i+1:])

    return result