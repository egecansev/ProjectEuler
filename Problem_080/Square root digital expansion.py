from decimal import *
from time import time


start = time()
getcontext().prec = 105
sums = []
for i in range(100):
    num = str(Decimal.sqrt(Decimal(i))).split('.')
    if len(num) > 1:
        num = num[0] + num[1]
        sums.append(sum(int(j) for j in num[:100]))
print(sum(sums))
end = time()
print("Time elapsed", end - start, "seconds")
