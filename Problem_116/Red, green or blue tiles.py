from time import time


def factorial(n):
    multiplicand = 1
    for m in range(2, n + 1):
        multiplicand *= m
    return multiplicand


def combination(n, m):
    return factorial(n) // (factorial(n - m) * factorial(m))


# Combination of indistinguishable balls into indistinguishable boxes
# https://math.stackexchange.com/questions/2522240/m-indistinguishable-balls-on-n-indistinguishable-boxes
start = time()
length = 50
total = 0
for tiles in range(2, 5):
    max_coloured = length // tiles
    for colour in range(1, max_coloured + 1):
        free = length - tiles * colour
        total += combination(colour + free, colour)
print(total)
end = time()
print('Time elapsed', end - start, 'seconds')
