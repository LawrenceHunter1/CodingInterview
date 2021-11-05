def mergeSort(array):
    if len(array) <= 1:
        return array
    middle = (len(array)+1) // 2
    left = mergeSort(array[:middle])
    right = mergeSort(array[middle:])
    return merge(left, right)

def merge(left, right):
    sorted = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
    return sorted + right[j:] + left[i:]