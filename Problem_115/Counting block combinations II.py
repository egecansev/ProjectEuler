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
limit = 10**6
min_length = 50
length = min_length
while True:
    max_reds = (length + 1) // (min_length + 1)
    total = 0
    for red in range(max_reds + 1):
        if red == 0:
            total += 1
        else:
            if red == 1:
                free = length - min_length
            else:
                free = length - ((min_length + 1) * red - 1)
            for i in range(free + 1):
                total += combination(red + free - 1 - i, red - 1) * combination(red + i, red)
    if total > limit:
        break
    length += 1
print(length)
end = time()
print('Time elapsed', end - start, 'seconds')
