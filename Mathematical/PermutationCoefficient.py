def permutationCoefficient(n, k):
    if (k > n):
        return 0
    if (n == 0 or k == 0):
        return 1
    return factorial(n) / (factorial(n-k))

def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x-1)