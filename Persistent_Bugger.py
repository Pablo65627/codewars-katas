def persistence(num):
    count = 0

    while num >= 10:
        product = 1
        for digit in str(num):
            product *= int(digit)
        
        num = product
        count += 1

    return count