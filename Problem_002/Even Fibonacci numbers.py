from time import time

start = time()
total = 2
limit = 4 * 10**6
i, j = 1, 2
while True:
    k = i + j
    if limit <= k:
        break
    elif not k % 2:
        total += k
    i = j
    j = k
print(total)
end = time()
print('Time elapsed', end - start, 'seconds')
