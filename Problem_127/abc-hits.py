from time import time
from math import gcd
from numpy import prod


def primes_sieve2(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return list(set(factors))


def radical(trio):
    all_factors = []
    for i in trio:
        if i in primes:
            all_factors.append(i)
        else:
            for j in prime_factors(i):
                all_factors.append(j)
    return prod(list(set(all_factors)))


def sieve(n):
    poss = list(range(length))
    facts = prime_factors(n)
    for fact in facts:
        poss[fact] = -1
        for n in range(fact*fact, length, fact):
            poss[n] = -1
    for n in range(length):
        index = length-n-1
        if poss[index] == -1:
            poss.pop(index)
    poss.pop(0)
    return poss, facts


start = time()
global length
length = 1000
primes = list(primes_sieve2(length))

total = 0
for c in [item for item in range(3, length) if item not in primes]:
    candidates, factors_c = sieve(c)
    for a in candidates:
        if a >= (c+1)//2:
            break
        b = c - a
        if b in candidates and gcd(a, b) == 1:
            if radical((a, b, c)) < c:
                total += c
print(total)
end = time()
print('Time elapsed', end - start, 'seconds')
