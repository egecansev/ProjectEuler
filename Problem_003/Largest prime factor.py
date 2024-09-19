from time import time


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif (n % 2 == 0) or (n % 3 == 0):
        return False
    i = 5
    while i*i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i = i + 6
    return True


def find_largest_prime_factor(n):
    for i in range(n):
        if is_prime(i):
            while not n % i:
                n //= i
        if n == 1:
            return i


start = time()
number = 600851475143
print(find_largest_prime_factor(number))
end = time()
print('Time elapsed', end - start, 'seconds')
