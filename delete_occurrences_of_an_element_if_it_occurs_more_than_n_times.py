def delete_nth(order,max_e):
    result = []
    counts = {}
    
    for num in order:
        counts[num] = counts.get(num, 0)
        if counts[num] < max_e:
            result.append(num)
            counts[num] += 1
    return result