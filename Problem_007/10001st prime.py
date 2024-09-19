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


start = time()
k = 10001
count = 0
m = 1
while count != k:
    m += 1
    if is_prime(m):
        count += 1
print(m)
end = time()
print('Time elapsed', end - start, 'seconds')
