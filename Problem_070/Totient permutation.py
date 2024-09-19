from itertools import combinations
import time


def is_prime(x):
    if x == 2: return True
    if x % 2 == 0: return False
    for n in range(3, int(x/2)+1):
        if x % n == 0:
            return False
    return True


start = time.time()
limit = 4*pow(10,3)     # To create a gap from the limit sqrt(10^7) in order to check greater numbers
prime = 2
primes = []
while prime < limit:
    if is_prime(prime):
        primes.append(prime)
    prime += 1
comb = list(combinations(reversed(primes), 2))
min = 100
for combination in comb:
    if combination[0]*combination[1] < pow(10,7) and sorted(str(combination[0]*combination[1])) == sorted(str((combination[0]-1)*(combination[1]-1))):
        ratio = (combination[0]*combination[1]) / ((combination[0]-1)*(combination[1]-1))
        if ratio < min:
            min = ratio
            number = combination[0]*combination[1]
print(number)
end = time.time()
print("Time elapsed" , end-start, "seconds")