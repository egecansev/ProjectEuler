from time import time
from numpy import gcd

def prime_factors (n):
    pfactors = [1]
    for i in range(2, n):
        if n**2 % i == 0:
            pfactors.append(i)
    return pfactors


start = time()
limit = 1.5 * 10**6
lengths = {}
m = 2
length = 0
while length <= limit:
    for n in range(1, m):
        if gcd(m, n) == 1 and (m % 2)*(n % 2) != 1:
            length = 2 * m * (m + n)
            base = length
            i = 2
            while length <= limit:
                if length not in lengths.keys():
                    count = 0
                else:
                    count = lengths[length]
                count += 1
                lengths[length] = count
                length = base * i
                i += 1
    m += 1
    length = 2 * m * (m + 1)
count = 0
for freq in lengths.values():
    if freq == 1:
        count += 1
print(count)
end = time()
print("Time elapsed", end-start, "seconds")
