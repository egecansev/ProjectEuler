from time import time


def factorial(n):
    fact = 1
    for m in range(1, n+1):
        fact *= m
    return fact


start = time()
f = str(factorial(100))
total = 0
for i in range(len(f)):
    total += int(f[i])
print(total)
end = time()
print('Time elapsed', end - start, 'seconds')
