from time import time
from math import factorial


def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))


start = time()
coord = []
i = 3
candidate = []
while True:
    for j in range(2, i+1):
        candidate.append([i, j, (i-1)*(j-1), abs(combination(i, 2) * combination(j, 2) - 2 * 10**6)])
    if combination(i, 2) * combination(j, 2) > 10 ** 8:
        break
    i += 1
print(sorted(candidate, key=lambda x: x[3])[0][2])
end = time()
print('Time elapsed', end - start, 'seconds')
