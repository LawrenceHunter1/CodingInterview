def binarySearch(array, element):
    start = 0
    end = len(array) - 1
    
    while start <= end:
        mid = (end + start) // 2

        if array[mid] < element:
            start = mid + 1
        
        elif array[mid] > element:
            end = mid - 1
        
        else:
            return True
    return False