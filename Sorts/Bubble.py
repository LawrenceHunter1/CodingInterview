def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def bubbleSortOpt(array):
    for i in range(len(array)):
        swap = False
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                swap = True
                array[j], array[j+1] = array[j+1], array[j]
        if not swap:
            return array
    return array