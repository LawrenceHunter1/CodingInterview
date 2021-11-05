def quickSort(array, low, high):
    # Haven't finished as no complete pass
    if (low < high):
        # Get the pivot then quick sort the left and right side recurively 
        p_i = partition(array, low, high)
        quickSort(array, low, p_i - 1)
        quickSort(array, p_i + 1, high)
    return array

def partition(array, low, high):
    # From beginning to end
    pivot = low
    for i in range(low + 1, high + 1):
        # Swap all less than or equal to the finding the value which 
        # divides the list into two halves
        if array[i] <= array[pivot]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[low] = array[low], array[pivot]
    return pivot

def quickSortHandler(array):
    return quickSort(array, 0, len(array) - 1)