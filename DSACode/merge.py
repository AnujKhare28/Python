def merge_array(left, right):
    result =[]
    i, j = 0,0

    n, m = len(left), len(right)
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < n:
        while i < n:
            result.append(left[i])
            i += 1
        #result.extend(left[i:])
    if j < m:
        while j < m:
            result.append(right[j])
            j += 1
        #result.extend(right[j:])
    return result

print(merge_array([1, 2, 3, 4, 5, 6, 8, 9],[1, 2, 3, 4, 5]))