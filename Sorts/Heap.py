def heapSort(array):
    length = len(array)
    for i in range(length // 2 - 1, -1, -1):
        array = heapify(array, length, i)

    for i in range(length - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        array = heapify(array, i, 0)
    
    return array

def heapify(array, length, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < length and array[i] < array[left]:
        largest = left

    if right < length and array[largest] < array[right]:
        largest = right
    
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        array = heapify(array, length, largest)
    
    return array