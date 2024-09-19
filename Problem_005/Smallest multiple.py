from time import time


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif (n % 2 == 0) or (n % 3 == 0):
        return False
    i = 5
    while i*i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i = i + 6
    return True


def is_divisible(n):
    for i in range(2, limit + 1):
        if n % i:
            return False
    return True


start = time()
limit = 20
base = 1
for x in range(limit + 1):
    if is_prime(x):
        base *= x
x = 1
while True:
    if is_divisible(x * base):
        break
    x += 1
print(x * base)
end = time()
print('Time elapsed', end - start, 'seconds')
