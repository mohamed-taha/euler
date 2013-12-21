import timeit, heapq

def primes3(max):
    multiples = set()
    primes = set([2])
    for i in range(2, max+1):
        if i not in multiples:
            primes.add(i)
            multiples.update(range(i ** 2, max+1, i))
    return primes

num_trials = 10
n = 1000000
print sorted(primes3(n))[10000]
