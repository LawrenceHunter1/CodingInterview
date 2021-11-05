def insertionSort(array):
    for i in range(1, len(array)):
        element = array[i]
        while i > 0 and array[i-1] > element:
            array[i] = array[i-1]
            i -= 1
            array[i] = element
    return array