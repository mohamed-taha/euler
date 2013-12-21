from itertools import count

def triangular_gen():
    num = 1
    for i in count(2):
        yield num
        num += i

def factors_of(n):
    if n == 1:
        yield 1
        return

    sqrt_n = int(n ** .5)
    yield 1
    yield n

    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            yield i
            yield n / i


it = triangular_gen()
while True:
    n = it.next()
    num_factors = len(sorted(factors_of(n)))
    if num_factors >= 500:
        print n, num_factors
        break