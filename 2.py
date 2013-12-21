def fib_iter(max):
    a, b = 1, 2
    while a < max:
        yield a
        a, b = b, a+b

print sum(x for x in fib_iter(4000000) if x % 2 == 0)