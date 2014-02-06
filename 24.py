import itertools

print ''.join(next(itertools.dropwhile(lambda x: x[0] < 999999, enumerate(itertools.permutations('0123456789'))))[1])