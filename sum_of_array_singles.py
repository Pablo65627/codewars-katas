def repeats(array):
    from functools import reduce
    return reduce((lambda x, y: x + y), [item for item in array if array.count(item) == 1])