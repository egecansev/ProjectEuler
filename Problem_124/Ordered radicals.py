from time import time


def all_divisors(i):
    divisors = []
    for j in primes:
        if i % j == 0:
            divisors.append(j)
    if not divisors:
        divisors.append(i)
        primes.append(i)
    return divisors


def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif (n % 2 == 0) or (n % 3 == 0):
        return False
    i = 5
    while i*i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i = i + 6
    return True


def all_multiples(l, n, m, s):
    for index in range(s, len(l)):
        factor = l[index]
        if n * factor <= limit:
            m.append(n * factor)
            m = all_multiples(l, n * factor, m, index)
        else:
            return m
    return m


def update_list(n):
    global order, target
    multiples = sorted(all_multiples(all_divisors(n), n, [n], 0))
    for multiple in multiples:
        order += 1
        if order == target:
            print(multiple)
            return
        numbers.remove(multiple)


start = time()
limit = 10 ** 5
target = 10 ** 4
numbers = list(range(2, limit + 1))
order = 1
primes = []

while numbers:
    update_list(numbers[0])
    if order == target:
        break
end = time()
print('Time elapsed', end - start, 'seconds')
