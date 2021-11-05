def maxDivide(a, b):
    while a % b == 0:
        a = a / b
    return a

def isUgly(n):
    n = maxDivide(n, 2)
    n = maxDivide(n, 3)
    n = maxDivide(n, 5)
    return 1 if n == 1 else 0

def getNUglyNo(n):
    i = 1
    count = 1
    if n <= 0:
        return []
        
    result = [1]

    while n > count:
        i += 1
        if isUgly(i):
            result.append(i)
            count += 1
    return result