from time import time
import pickle
import os

start = time()
if "primes" not in os.listdir():
    primes=[2]
    for i in range(1,int(pow(10,6)/2)+1):
        if isprime(2*i+1):
            primes.append(2*i+1)
    pickle.dump(primes,open("primes","wb"))
else:
    primes=pickle.load(open("primes","rb"))

number = 1
limit = pow(10, 6)
for prime in primes:
    number *= prime
    if number > limit:
        number = int(number / prime)
        break
print(number)

end = time()
print('Time elapsed', end - start, 'seconds')