from time import time


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


def permutation(x, y):
    return factorial(x+y)/(factorial(x)*factorial(y))


start = time()
print(int(permutation(20, 20)))
end = time()
print('Time elapsed', end - start, 'seconds')
