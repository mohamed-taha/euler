def fib():
    a, b = 1, 1
    yield a
    yield b
    while True:
        a, b = b, a+b
        yield b

fibit = fib()
x = 0
i = 0
while len(str(x)) < 1000:
    x = fibit.next()
    i+=1
print x, i