def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def permutations(n, p):
    return factorial(n) / factorial(p)

def combinations(n, p):
    return permutations(n, p) / factorial(n - p)

print combinations(4, 2)
print combinations(40, 20)