def is_palindrome(x):
    x = str(x)
    return x == x[::-1]

def find_palindrome(n=1000):
    for i in range(100, n):
        for j in range(100, n):
            x = i * j
            if is_palindrome(x):
                yield x

print max(find_palindrome())
