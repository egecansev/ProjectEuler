from time import time

start = time()
total = 0
for a in range(3, 1001):
    if a % 2:
        total += a * (a - 1)
    else:
        total += a * (a - 2)
print(total)
end = time()
print('Time elapsed', end - start, 'seconds')
