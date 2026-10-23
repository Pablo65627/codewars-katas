def first_n_smallest(arr, n):
    indexed_arr = list(enumerate(arr))
    
    sorted_by_val = sorted(indexed_arr, key=lambda x: x[1])
    
    smallest_n = sorted_by_val[:n]
    
    smallest_n.sort(key=lambda x: x[0])
    
    return [x[1] for x in smallest_n]