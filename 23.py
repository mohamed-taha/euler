def divisors_of(n):
    divisors = [1]
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            divisors.append(i)
            if (n / i) != i:
                divisors.append(n / i)
    return divisors

def is_abundant(n):
    return n < sum(divisors_of(n))

ss = 0
abundants = []
for i in range(2, 28124):
    if is_abundant(i):
        abundants.append(i)

sums_of_2 = set(x+y for x in abundants for y in abundants if x+y <= 28124)
print sum(i for i in range(1, 28124) if i not in sums_of_2)
