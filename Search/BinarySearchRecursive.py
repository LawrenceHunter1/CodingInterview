def binarySearch(array, element, start, end):
    if start > end:
        return False
    
    mid = (start + end) // 2
    if element == array[mid]:
        return True
    
    if element < array[mid]:
        return binarySearch(array, element, start, mid - 1)
    else:
        return binarySearch(array, element, mid + 1, end)

def binarySearchHandler(array, element):
    return binarySearch(array, element, 0, len(array) - 1)