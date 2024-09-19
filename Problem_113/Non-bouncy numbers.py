from time import time


def factorial(n):
    multiplicand = 1
    for m in range(2, n + 1):
        multiplicand *= m
    return multiplicand


def combination(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))


# https://codereview.stackexchange.com/questions/110450/finding-non-bouncy-numbers-under-10x
start = time()
target = 100
total = 0
for length in range(1, target + 1):
    for i in range(2, min(length + 1, 11)):
        total += 2 * (combination(length - 1, i - 1) * combination(10, i))\
                 - combination(length - 1, i - 1) * combination(9, i - 1)
    total += 9
print(total)
end = time()
print('Time elapsed', end - start, 'seconds')
