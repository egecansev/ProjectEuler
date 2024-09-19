from time import time


start = time()
for m in range(1, 1001):
    if not 1000 % m:
        n = 1000 // m - m
        if 0 < n < m:
            print(m * n * (m ** 4 - n ** 4) // 4)
            break
end = time()
print('Time elapsed', end - start, 'seconds')
