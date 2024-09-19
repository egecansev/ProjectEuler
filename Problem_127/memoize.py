from time import time
from math import gcd
from numpy import prod


def num2fact():
    for i in range(2, length):
        factors_table[i] = prime_factors(i)


def fact2num():
    for p in primes:
        numbers_table[p] = []
    for i, facts in factors_table.items():
        for fact in facts:
            numbers_table[fact].append(i)


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


def sieve(x):
    span = (x+1)//2
    poss = list(range(span))
    facts = prime_factors(x)
    for fact in facts:
        if fact >= span:
            break
        poss[fact] = -1
        for y in range(fact, span, fact):
            poss[y] = -1
    for y in range(span):
        index = span-y-1
        if poss[index] == -1:
            poss.pop(index)
    poss.pop(0)
    return poss, facts


start = time()
global length
length = 1000
primes = primes_sieve2(length)
factors_table = {}
numbers_table = {}
num2fact()
end = time()
print('Time elapsed', end - start, 'seconds')
fact2num()
end = time()
print('Time elapsed', end - start, 'seconds')
factor_dict = {1: [1]}
for j in range(3, length):
    for i in range(2, j):
        gcd(length, i)
end = time()
print('Time elapsed', end - start, 'seconds')


for i in range(2, length):
    factor_dict[i] = prime_factors(i)
end = time()
print('Time elapsed', end - start, 'seconds')
limit = int(length**0.5)+1
primes = list(primes_sieve2(12000))
end = time()
print('Time elapsed', end - start, 'seconds')
visited = []
total = 0
for n in primes:
    m = 1
    c = n * n
    while c < length:
        if c in visited:
            c = m * n * n
            m += 1
            continue
        visited.append(c)
        candidates, factors_c = sieve(c)
        for a in candidates:
            if radical((a, c-a, c)) < c:
                #print(a,c-a,c)
                total += c
        c = m * n * n
        m += 1

print(total)
end = time()
print('Time elapsed', end - start, 'seconds')
