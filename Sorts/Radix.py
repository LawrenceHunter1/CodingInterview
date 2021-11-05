def radixSort(array):
    length = len(array)
    if length <= 1:
        return array

    max = array[0]
    for item in array:
        if item > max:
            max = item

    exp = 1
    while max // exp > 0:
        array = countingSort(array, exp)
        exp *= 10

    return array

def countingSort(array, exp):
    length = len(array)
    output = [0] * length
    count = [0] * 10

    for i in range(0, length):
        index = array[i] // exp
        count[index % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    i = length - 1
    while i >= 0:
        index = array[i] // exp
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
    
    for i in range(0, length):
        array[i] = output[i]

    return array