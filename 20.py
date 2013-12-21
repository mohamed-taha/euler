def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1), 1)

def sum_fact_digit(n):
    return sum(int(c) for c in str(factorial(n)))

print sum_fact_digit(10)
print sum_fact_digit(100)
