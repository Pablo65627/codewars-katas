from functools import reduce


def to_camel_case(string):

    try:
        return reduce(
                      (lambda x, y: x[:-1] + x[-1].upper() if y in ['-', '_'] else x + y),
                       string[::-1])[::-1]
    except TypeError:
        return ''