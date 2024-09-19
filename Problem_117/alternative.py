from time import time


def factorial(n):
    multiplicand = 1
    for m in range(2, n + 1):
        multiplicand *= m
    return multiplicand


def combination(n, m):
    return factorial(n) // (factorial(n - m) * factorial(m))


def permutation(n):
    divisor = 1
    for item in n:
        divisor *= factorial(item)
    return factorial(sum(n)) // divisor


# Combination of indistinguishable balls into indistinguishable boxes
# https://math.stackexchange.com/questions/2522240/m-indistinguishable-balls-on-n-indistinguishable-boxes
start = time()
length = 50
total = 1
max_coloured_dict = {}
# Single coloured
for tiles in range(2, 5):
    max_coloured = length // tiles
    max_coloured_dict[tiles] = max_coloured
    for colour in range(1, max_coloured + 1):
        free = length - tiles * colour
        total += combination(colour + free, colour)
# Double coloured
for tile1 in range(2, 5):
    for tile2 in range(tile1 + 1, 5):
        for n1 in range(1, max_coloured_dict[tile1]):
            remaining = length - tile1 * n1
            max_n2 = remaining // tile2
            for n2 in range(1, max_n2 + 1):
                colour = n1 + n2
                free = remaining - tile2 * n2
                total += combination(colour + free, colour) * permutation([n1, n2])
# Triple coloured
tile1, tile2, tile3 = 2, 3, 4
for n1 in range(1, max_coloured_dict[tile1]):
    remaining1 = length - tile1 * n1
    max_n2 = remaining1 // tile2
    for n2 in range(1, max_n2 + 1):
        remaining2 = remaining1 - tile2 * n2
        max_n3 = remaining2 // tile3
        for n3 in range(1, max_n3 + 1):
            colour = n1 + n2 + n3
            free = remaining2 - tile3 * n3
            total += combination(colour + free, colour) * permutation([n1, n2, n3])

print(total)
end = time()
print('Time elapsed', end - start, 'seconds')
