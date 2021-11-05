def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    else:
        result = [0, 1]
        count = 0
        while count < n:
            result.append(result[count] + result[count+1])
            count += 1