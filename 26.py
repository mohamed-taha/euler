# NOT WORKING!!!
def recurring_cycle(n):
    x = 1
    divisors = []
    import ipdb; ipdb.set_trace()
    while x != 0:
        x *= 10
        d = x // n
        if d == 0:
            divisors.append([d, x])
            continue
        x %= n

        if [d, x] in divisors:
            i = divisors.index(d)
            return divisors[:i], divisors[i:]
        divisors.append([d, x])
    return divisors, []


#print max(range(2, 1000), key=lambda x: len(recurring_cycle(x)[1]))

#print recurring_cycle(38)
print recurring_cycle(983)
print recurring_cycle(70)
print recurring_cycle(700)
