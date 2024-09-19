from time import time


start = time()
limit = 100
print((limit * (limit + 1) // 2) ** 2 - limit * (limit + 1) * (2 * limit + 1) // 6)
end = time()
print('Time elapsed', end - start, 'seconds')
