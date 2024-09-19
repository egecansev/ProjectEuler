from time import time


def is_prime(n):
    if n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i = i + 6
    return True


start = time()
limit = 10**10
count = 2
a = 5
while True:
    if is_prime(a):
        count += 1
        if count % 2:
            if limit < 2 * count * a:
                print(count)
                break
    a += 2
end = time()
print('Time elapsed', end - start, 'seconds')
