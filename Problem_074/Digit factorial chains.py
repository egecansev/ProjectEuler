from math import factorial
from time import time

def digit_factorial(n):
    sum = 0
    for digit in str(n):
        sum += factorial(int(digit))
    return sum

start = time()
count = 0
for i in range(pow(10,6)):
    number = i
    chain = []
    chain.append(number)
    while True:
        new = digit_factorial(chain[-1])
        if new in chain:
            break
        chain.append(new)
    if len(chain) == 60:
        #print(chain)
        count += 1
print(count)
end = time()
print("Time elapsed", end-start, "seconds")