def solution(args):
    result = []
    start = prev = args[0]

    for num in args[1:]:
        if num == prev + 1:
            prev = num
        else:
            if prev - start >= 2:
                result.append(f"{start}-{prev}")
            else:
                result.extend(str(x) for x in range(start, prev + 1))

            start = prev = num

    # Add the final sequence
    if prev - start >= 2:
        result.append(f"{start}-{prev}")
    else:
        result.extend(str(x) for x in range(start, prev + 1))

    return ",".join(result)