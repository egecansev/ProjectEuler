from time import time
from numpy import log2, gcd

start = time()
times = log2(pow(10, 6)/7)
den = 7*pow(2, int(times))
num = 3*pow(2, int(times))-1
top = int(3 * pow(10, 6) / 7)
maximum = 3 / 7
new = num / den
key = []
for d in range(den + 1, pow(10, 6)+1):
    n = int(maximum * d)
    for n in range(num, d):
        ratio = n/d
        if ratio >= maximum:
            break
        elif ratio > new:
            new = ratio
            key = [n, d]
            num = n
if key:
    print(int(key[0] / gcd(key[0], key[1])))
end = time()
print("Time elapsed", end-start, "seconds")
