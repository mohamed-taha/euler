import math

def primes(max):
    '''generate primes less than max'''
    max = int(math.sqrt(max - 2))
    nums = [False, False] + [True] * max
    n = 2
    while n < max:
        # All elements divisible by n are not primes
        i = n + n
        ####print i, n, max, ((max - i) / n), len(nums[i::n])
        ####nums[i::n] = [False] * ((max - i) / n)
        while i < max:
            nums[i] = False
            i += n
        # Find the next prime
        n += 1
        while n < max and not nums[n]:
            n += 1

    return [i for i in range(max) if nums[i]]

#n = 13195
n = 600851475143
print [x for x in primes(n) if n % x == 0]
