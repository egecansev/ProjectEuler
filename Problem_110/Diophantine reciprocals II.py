from time import time


def find_necessary_primes(i):
    count = 1
    value = 2
    while value <= i:
        value = 3 * value - 1
        count += 1
    prime_set = []
    i = 2
    while len(prime_set) != count:
        f = 1
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                f = 0
                break
        if f:
            prime_set.append(i)
        i += 1
    return prime_set


def list_multiplication(i):
    a = 1
    for item in i:
        a *= item
    return a


# https://en.wikipedia.org/wiki/Divisor_function
def sigma_0(pf):
    pf = [2 * i + 1 for i in pf]
    return (list_multiplication(pf) + 1) // 2


def get_number(p, pf):
    num = 1
    for n in range(len(pf)):
        num *= p[n] ** pf[n]
    return num


def loop_primes(p, i, level, n, comp, lim, previous_number):
    if level == len(p) - 1:
        return
    else:
        base_value = n
        j = 1
        level += 1
        while j <= i and base_value * (p[level] ** j) < lim:
            n = base_value * p[level] ** j
            if previous_number < n:
                comp.append(n)
            loop_primes(p, j, level, n, comp, lim, previous_number)
            j += 1
        return


# It can be used for integer partitioning
def sort_composite_numbers(p, lim, previous_number):
    composites = []
    i = 1
    while p[0] ** i < lim:
        num = p[0] ** i
        if previous_number < num:
            composites.append(num)
        loop_primes(p, i, 0, num, composites, lim, previous_number)
        i += 1
    composites = get_prime_factors(sorted(composites))
    return composites


def get_prime_factors(comp):
    prime_facts = []
    for item in comp:
        fact = []
        for prime in primes:
            count = 0
            while item % prime == 0:
                item //= prime
                count += 1
            fact.append(count)
            if item == 1:
                prime_facts.append(fact)
                break
    return prime_facts


start = time()
limit = 4 * 10**6
primes = find_necessary_primes(limit)
necessary_primes = list(primes)
min_number = list_multiplication(primes)
prev_factor = []
while len(primes) > 1:
    flag = 0
    primes.pop()
    composite_factors = sort_composite_numbers(primes, min_number // list_multiplication(primes),
                                               get_number(necessary_primes, prev_factor))
    for factor in composite_factors:
        prime_factors = [1] * len(primes)
        for m in range(len(factor)):
            prime_factors[m] += factor[m]
        if sigma_0(prime_factors) > limit:
            number = get_number(primes, prime_factors)
            if number < min_number:
                min_number = number
                flag = 1
                prev_factor = factor
                break
        if flag:
            break
print(min_number)
end = time()
print('Time elapsed', end - start, 'seconds')
