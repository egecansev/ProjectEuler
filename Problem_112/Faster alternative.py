from time import time


def is_bouncy(n):
    order = 0
    indecisive = 0
    for i in range(len(n) - 1):
        if int(n[i]) < int(n[i + 1]):
            order = 1
            break
        elif int(n[i]) > int(n[i + 1]):
            order = -1
            break
        else:
            indecisive += 1
    if order:
        for i in range(indecisive, len(n) - 1):
            if 0 > order * (int(n[i + 1]) - int(n[i])):
                return True
    return False


def factorial(n):
    multiplicand = 1
    for m in range(2, n + 1):
        multiplicand *= m
    return multiplicand


def combination(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))


# https://codereview.stackexchange.com/questions/110450/finding-non-bouncy-numbers-under-10x
start = time()

# From Non-bouncy numbers
length = 1
total = 0
while True:
    for i in range(2, min(length + 1, 11)):
        total += 2 * (combination(length - 1, i - 1) * combination(10, i))\
                 - combination(length - 1, i - 1) * combination(9, i - 1)
    total += 9
    if total / 10 ** length < 0.01:
        break
    prev_total = total
    length += 1

# From Bouncy numbers
number = 10 ** (length - 1)
count = number - prev_total - 1
while True:
    if is_bouncy(str(number)):
        count += 1
    if count == 0.99 * number:
        break
    number += 1
print(number)
end = time()
print('Time elapsed', end - start, 'seconds')
