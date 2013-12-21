def gcb2(a, b):
    if b == 0:
        return a
    return gcb2(b, a % b)

def lcm2(a, b):
    return (a * b) / gcb2(a, b)

def lcm(n):
    if len(n) == 1:
        return n[0]
    if len(n) == 2:
        return lcm2(n[0], n[1])
    return lcm2(lcm2(n[0], n[1]), lcm(n[2:]))

print lcm(range(1, 21))