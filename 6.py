def sum_squares_till(n):
    return sum(x ** 2 for x in range(n + 1))

def square_sums(n):
    return sum(range(n + 1)) ** 2

print square_sums(10) - sum_squares_till(10)
print square_sums(100) - sum_squares_till(100)