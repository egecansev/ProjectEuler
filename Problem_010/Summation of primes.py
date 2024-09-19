from time import time


def primes_sieve2(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False


start = time()
lim = 2 * 10 ** 6
print(sum(primes_sieve2(lim)))
end = time()
print('Time elapsed', end - start, 'seconds')
