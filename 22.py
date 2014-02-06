import string

def name_value(name):
    return sum((string.ascii_letters.index(c.lower())+1) for c in name)

names = sorted(name.strip('"') for name in open('names.txt').read().split(','))

print sum(name_value(name)*(order+1) for order, name in enumerate(names))