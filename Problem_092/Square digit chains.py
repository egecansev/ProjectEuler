# Faster with c++, check the alternative.py
from time import time


def digit_square_sum(n):
    total = 0
    for digit in str(n):
        total += int(digit) ** 2
    return total


start = time()
limit = 10 ** 7
ones = [1]
others = [89]
for new in range(2, 568):
    path = []
    while True:
        if new in ones:
            ones += path
            break
        elif new in others:
            others += path
            break
        if new < 568:
            path.append(new)
        new = digit_square_sum(new)

count = len(others)
for i in range(568, limit):
    if digit_square_sum(i) in others:
        count += 1
print(count)
end = time()
print("Time elapsed", end - start, "seconds")
