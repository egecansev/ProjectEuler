from math import sqrt
from time import time


def is_prime(n):
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


def merge_check(a, b):
    m = int(str(a) + str(b))
    if not is_prime(m):
        return False
    n = int(str(b) + str(a))
    if not is_prime(n):
        return False
    return True


def extract():
    for x in primes:
        for y in primes[primes.index(x) + 1:]:
            if merge_check(x, y):
                for z in primes[primes.index(y) + 1:]:
                    if merge_check(x, z) and merge_check(y, z):
                        for t in primes[primes.index(z) + 1:]:
                            if merge_check(x, t) and merge_check(y, t) and merge_check(z, t):
                                for u in primes[primes.index(t) + 1:]:
                                    if merge_check(x, u) and merge_check(y, u) and merge_check(z, u) and merge_check(t,
                                                                                                                     u):
                                        print(x + y + z + t + u)
                                        return 0


start = time()
primes = []
for i in range(10000):
    if i > 2:
        if is_prime(i):
            primes.append(i)
primes.remove(5)
extract()
end = time()
print("Time elapsed", end - start, "seconds")
