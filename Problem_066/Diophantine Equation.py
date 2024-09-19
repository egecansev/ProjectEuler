from math import sqrt
import time
from decimal import *


def get_squares(value):
    approx = Decimal(value).sqrt()
    approx = int(approx)
    neighbours = [approx, approx + 1]
    return neighbours


def is_square(sqs, xx, candidate):
    for square in sqs:
        if xx * xx - candidate * square * square == 1:
            return True
        elif xx * xx - candidate * square < 1:
            return False
    return False


def convergent(gorgonzola, d):
    num = gorgonzola.pop(0)
    den = 1
    j = 0
    while True:
        dude = Decimal(num * num - 1) / d
        if dude == int(dude):
            interval = get_squares(dude)
            if is_square(interval, num, d):
                break
        num, den = den, num
        num = gorgonzola[j] * den + num
        j += 1
        if j == len(gorgonzola):
            j = 0
    target = num
    return target


start = time.time()
getcontext().prec = 100
fractions = {}
for m in range(2, 1001):
    a0 = int(sqrt(m))
    if int(a0 * a0) == m:
        continue
    guttus = [a0]
    k = 1
    n = a0
    while True:
        x = int(k / (sqrt(m) - n))
        y = (m - n * n) / k
        z = -(n - x * (m - n * n) / k)
        a = x
        k = int(y)
        n = int(z)
        guttus.append(a)
        if guttus[-1] == 2 * a0:
            break
    fractions[m] = guttus
for i, fraction in fractions.items():
    if len(fraction) % 2:  # EVEN PERIOD
        x = convergent(fraction, i)
    else:  # ODD PERIOD
        x = convergent(fraction, i)
    if x > y:
        solution = i
        y = x
end = time.time()
print(solution)
print("Time elapsed is ", end - start, " seconds")
