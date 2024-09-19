from time import time
from numpy import gcd


start = time()
limit = 12000
cnt = 0
minimum = 1 / 3
maximum = 1 / 2
for d in range(4, limit + 1):
    n = int(minimum * d)
    while n / d < minimum:
        n += 1
    while n / d < maximum:
        if gcd(n, d) == 1:
            cnt += 1
        n += 1
print(cnt)
end = time()
print("Time elapsed", end-start, "seconds")