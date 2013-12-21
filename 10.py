def primes3(max):
    multiples = set()
    primes = set([2])
    for i in range(2, max+1):
        if i not in multiples:
            primes.add(i)
            multiples.update(range(i ** 2, max+1, i))
    return primes


print sum(primes3(2000000))