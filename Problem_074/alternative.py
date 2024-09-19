from math import factorial
from time import time


def digit_factorial(n):
    sum = 0
    for digit in str(n):
        sum += factorial(int(digit))
    return sum


start = time()
count = 0
chains = {}
for i in range(2,pow(10,6)):
    chain = []
    chain.append(i)
    while True:
        new = digit_factorial(chain[-1])
        if new in chains.keys():
            if chains.get(new) + len(chain) != 60:
                chains[i] = len(chain) + chains.get(new)
            else:
                count += 1
                chains[i] = 60
            break
        if new in chain:
            chains[i] = len(chain)
            break
        chain.append(new)
print(count)
end = time()
print("Time elapsed", end-start, "seconds")
