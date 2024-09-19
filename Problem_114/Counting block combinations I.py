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
max_reds = (length + 1) // 4
total = 0
for red in range(max_reds + 1):
    if red == 0:
        total += 1
    else:
        if red == 1:
            free = length - 3
        else:
            free = length - (4 * red - 1)
        for i in range(free + 1):
            total += combination(red + free - 1 - i, red - 1) * combination(red + i, red)
print(total)
end = time()
print('Time elapsed', end - start, 'seconds')
