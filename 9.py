import sys

for c in range(0, 1001):
    c2 = c ** 2
    for b in range(0, c):
        b2 = b ** 2
        for a in range(0, b):
            if (a**2 + b2 == c2) and (a+b+c == 1000):
                print a*b*c
                sys.exit()