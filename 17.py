nums_words_small = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}

multiples = {
    1: '',
    10: '',
    100: 'hundred'
}

def combine_with_and(parts):
    return parts[:-1] + ['and'] + [parts[-1]]

def num_in_words(n, max=1000):
    if n == 1000:
        return 'onethousand'
    n_analyzed = [int(i) for i in '{:03d}'.format(n)]
    result = []
    if n_analyzed[0]:
        result.append(nums_words_small[n_analyzed[0]])
        result.append('hundred')
        if n_analyzed[1] or n_analyzed[2]:
            result.append('and')
    if (n_analyzed[1] * 10 + n_analyzed[2]) in nums_words_small:
        result.append(nums_words_small[n_analyzed[1] * 10 + n_analyzed[2]])
        return ''.join(result)
    if n_analyzed[1]:
        result.append(nums_words_small[n_analyzed[1] * 10])
    if n_analyzed[2]:
        result.append(nums_words_small[n_analyzed[2]])
    return ''.join(result)

for n in (1, 2, 3, 4, 5, 8, 10, 14, 51, 100, 513, 987, 342, 115):
    print n, '=>', num_in_words(n), len(num_in_words(n))

print sum(len(num_in_words(n)) for n in range(1, 1001))

