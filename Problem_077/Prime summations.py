from time import time
from sympy import primerange


def count_ways(total, coins):
    if total < 0:
        return 0
    if total == 0:
        return 1
    if len(coins) <= 0:
        return 0
    return count_ways(total - coins[-1], coins) + count_ways(total, coins[:-1])


start = time()
target = 2
while True:
    ways = count_ways(target, list(primerange(1, target)))
    if ways > 5000:
        break
    target += 1
print(target)
end = time()
print("Time elapsed", end-start, "seconds")
