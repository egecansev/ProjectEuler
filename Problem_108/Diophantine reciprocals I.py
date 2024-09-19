# FOR THE FASTER VERSION, CHECK PROBLEM 110
from time import time
from numpy import gcd


def memoization(divisors):
    global memoize
    for divisor in divisors:
        values = []
        if divisor not in memoize.keys():
            for couple in all_gcd_divisors(divisor):
                values.append(couple)
            memoize[divisor] = values
    return


def all_gcd_divisors(i):
    divisors = []
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0 and gcd(j, i // j) == 1:
            divisors.append([j, i//j])
    divisors.append([1, i])
    return divisors


def all_divisors(i):
    divisors = [1]
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            divisors.append(j)
            if j * j != i:
                divisors.append(i // j)

    divisors.append(i)
    return divisors


def count_gcd(i):
    count = 0
    divisors = all_divisors(i)
    memoization(divisors)
    for divisor in divisors:
        for value in memoize[divisor]:
            if i * sum(value) % divisor == 0:
                count += 1
    return count


start = time()
solutions_count = 0
limit = 1000
n = 1
memoize = {}
while solutions_count < limit:
    n += 1
    solutions_count = count_gcd(n)
print(n)
end = time()
print('Time elapsed', end - start, 'seconds')
