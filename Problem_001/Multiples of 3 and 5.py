from time import time

start = time()
limit = 1000
print(sum([i for i in range(limit) if i % 3 == 0 or i % 5 == 0]))
end = time()
print('Time elapsed', end - start, 'seconds')
