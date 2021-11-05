def bucketSort(array):
    if len(array) <= 1:
        return array

    no_buckets = 5

    max_ele = max(array)
    min_ele = min(array)

    rnge = (max_ele - min_ele) / no_buckets

    result = []

    for i in range(no_buckets):
        result.append([])

    for i in range(len(array)):
        diff = (array[i] - min_ele) / rnge - int((array[i] - min_ele) / rnge)
        if (diff == 0 and array[i] != min_ele):
            result[int((array[i] - min_ele) / rnge) - 1].append(array[i])
        else:
            result[int((array[i] - min_ele) / rnge)].append(array[i])
          
    
    for i in range(len(result)):
        if len(result[i]) != 0:
            result[i].sort()

    k = 0
    for lst in result:
        if lst:
            for i in lst:
                array[k] = i
                k = k+1

    return array