from time import time
from math import gcd
from numpy import prod


def primes_sieve2(lim):
    a = [True] * lim
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for n in range(i * i, lim, i):
                a[n] = False


# def a_sieve(c):
#     lim = c//2
#     yield 1
#     if lim < 2:
#         raise StopIteration
#     a = [True] * (lim - 2)
#     for i in prime_factors(c):
#         if i > lim:
#             a[i] = False
#
#     for (i, is_prime) in enumerate(a):
#         if is_prime:
#             i += 2
#             for n in range(i, lim//2, i):
#                 a[n] = False
#         else:
#             yield i


def a_sieve(c):
    lim = (c+1)//2

    a = list(range(lim))
    primes = prime_factors(c)
    if primes[0] >= lim:
        return [1]
    for i in primes:
        for n in range(i, lim, i):
            a[n] = -1

    for i in range(1, lim):
        if a[lim-i] == -1:
            a.pop(lim-i)
    a.pop(0)
    return a

def generate_c(prime):
    j = prime * prime
    i_lim = limit//j + 1
    for i in range(1, i_lim):
        cs.append(i * j)

def add_child(x):
    tree.append([2 * x[0] - x[1], x[0]])
    tree.append([2 * x[0] + x[1], x[0]])
    tree.append([x[0] + 2 * x[1], x[1]])


def generate_tree():
    for child in tree:
        if sum(child) < limit:
            add_child(child)
    else:
        return


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


start = time()
global limit
limit = 1000
primes = primes_sieve2(int(limit**0.5 + 1))
cs = []
# tree = [[2, 1]]
# generate_tree()
# print(len(tree))
for c in primes:
    generate_c(c)
cs = sorted(set(cs))
if cs[-1] == limit:
    cs.pop(-1)
print(len(cs))
count = 0
say = 0
for c in cs:
    for a in a_sieve(c):
        if radical([a, c-a, c]) < c:
            print(a, c-a, c)
            say += 1
            count += c
print(count)
print(say)
end = time()
print('Time elapsed', end - start, 'seconds')
