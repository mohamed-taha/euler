import timeit

def divisible_by(n, x):
    return [i for i in range(1, n) if i % x == 0]

def sum_range(n):
    return n * (n - 1) / 2

def sum_divisible_by(n, x):
    y = (n - 1) // x
    return x * sum_range(y+1)


# Performance Evaluation
for n in [10, 100, 1000, 3000]:
    print n,  '=>', sum(set(divisible_by(n, 3) + divisible_by(n, 5)))
    print n, '=>', sum_divisible_by(n, 3) + sum_divisible_by(n, 5) - sum_divisible_by(n, 15)