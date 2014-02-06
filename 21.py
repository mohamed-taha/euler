def d(n):
    return reduce(lambda x, y: x+y, divisors_of(n))

def divisors_of(n):
    divisors = [1]
    for i in range(2, int(n**.5)):
        if n % i == 0:
            divisors.extend((i, n / i))
    return divisors

print divisors_of(220), d(220)
print divisors_of(284), d(284)

amicable_pairs = []
for a in range(2, 10001):
    b = d(a)
    if a == d(b) and a != b:
        print a, b
        amicable_pairs.extend((a, b))

print sum(set(amicable_pairs))
