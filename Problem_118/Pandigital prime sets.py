from time import time
from itertools import permutations


def is_prime(n):
    if n in memo.keys():
        return memo[n]
    if n < 2:
        memo[n] = False
        return False
    elif n < 4:
        memo[n] = True
        return True
    elif (n % 2 == 0) or (n % 3 == 0):
        memo[n] = False
        return False
    i = 5
    while i*i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            memo[n] = False
            return False
        i = i + 6
    memo[n] = True
    return True


def find_prime(index, primes, all_primes):
    if index == 9:
        all_primes.append(sorted(primes))
        return primes
    for i in range(index + 1, 10):
        pan = get_number(pandigital[index:i])
        if is_prime(pan):
            primes.append(pan)
            find_prime(i, primes, all_primes)
            primes.pop()
    return all_primes


def get_number(p):
    return int(''.join(p))


start = time()
string = ""
distinct_sets = []
memo = {}
for a in range(1, 10):
    string += str(a)
for pandigital in permutations(string):
    if pandigital[-1] in ["1", "3", "5", "7", "9"] or \
            (pandigital[-1] == "2" and pandigital[-2] in ["1", "3", "5", "7", "9"]):
        prime_set = find_prime(0, [], [])
        if prime_set:
            while prime_set:
                distinct_sets.append(prime_set.pop())
distinct_sets = set(tuple(i) for i in distinct_sets)
print(len(distinct_sets))
end = time()
print('Time elapsed', end - start, 'seconds')
