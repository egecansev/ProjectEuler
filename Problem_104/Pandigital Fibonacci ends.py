from time import time


def fast_fibonacci(n):
    if memoize[n] != init:
        return memoize[n]
    if n == 0:
        memoize[n] = 0
        return 0
    elif n == 1:
        memoize[n] = 1
        return 1
    k = (n + 1) // 2
    a = fast_fibonacci(k)
    b = fast_fibonacci(k-1)
    if n % 2:
        memoize[n] = a**2 + b**2
        return a**2 + b**2
    else:
        memoize[n] = a * (2 * b + a)
        return a * (2 * b + a)


def is_pandigital(n):
    n = set(str(n))
    if '0' not in n and len(n) == 9:
        return True
    return False


start = time()
init = -1
memoize = [init] * 10 ** 6
Fibonacci = [1, 1]
length = 2
while len(str(Fibonacci[-1])) != 9:
    Fibonacci.append(Fibonacci.pop(0) + Fibonacci[0])
    length += 1
while True:
    if is_pandigital(str(Fibonacci[1])) and is_pandigital(str(fast_fibonacci(length))[:9]):
        break
    Fibonacci.append((Fibonacci.pop(0) % (10**9) + Fibonacci[0] % (10**9)))
    length += 1
print(length)
end = time()
print('Time elapsed', end - start, 'seconds')
