
def collatz(n):
    yield n
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1

        yield n

def iter_len(it):
    return sum(1 for _ in it)

print max(range(2, 1000000), key=lambda n: iter_len(collatz(n)))