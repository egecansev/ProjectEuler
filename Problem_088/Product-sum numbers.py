from time import time
from sympy import primerange
from copy import deepcopy


def get_factorization(candy):
    unique_prime_set = set(prime_facts.get(candy))
    for prime in unique_prime_set:
        multiplicand = candidate / prime
        if multiplicand in primes:
            break
        if multiplicand not in all_factors.keys():
            get_factorization(multiplicand)
        factors = all_factors.get(multiplicand)
        for factor in factors:
            for i in range(len(factor)):
                new_factor = deepcopy(factor)
                new_factor[i] = prime * new_factor[i]
                new_factor = sorted(new_factor)
                if new_factor not in all_factors[candy]:
                    all_factors[candy].append(new_factor)
            new_factor = sorted([prime] + factor)
            if new_factor not in all_factors[candy]:
                all_factors[candy].append(new_factor)


def get_prime_factors():
    prime_factors = []
    number = candidate
    flag = 0
    for prime in primes:
        while number % prime == 0:
            number /= prime
            prime_factors.append(prime)
            if number in prime_facts.keys():
                prime_factors = prime_factors + prime_facts.get(number)
                flag = 1
                break
        if number == 1 or flag == 1:
            prime_facts[candidate] = prime_factors
            return prime_facts


def calc_size(factor):
    length = len(factor)
    total = sum(factor)
    gap = candidate - total
    return length + gap


start = time()
primes = list(primerange(1, 15000))
limit = 12000
k = list(range(2, limit + 1))
candidate = 3
prime_facts = {}
all_factors = {}
result = 0
while k:
    main_flag = 0
    candidate += 1
    if candidate in primes:
        continue
    prime_facts = get_prime_factors()
    all_factors[candidate] = [prime_facts.get(candidate)]
    original_size = calc_size(prime_facts.get(candidate))
    get_factorization(candidate)
    if original_size >= k[0]:
        for group in all_factors.get(candidate):
            size = calc_size(group)
            if size in k:
                k.remove(size)
                main_flag = 1
            if not k or k[0] > original_size:
                break
        if main_flag:
            result += candidate

print(result)
end = time()
print('Time elapsed', end - start, 'seconds')
