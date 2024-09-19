import timeit
import math


def isprime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True


start=timeit.default_timer()
k=1
diagonals=[]
increment=0
dim=1
prime_count=0

while True:
    increment+=2
    diag=0
    for i in range(3):
        if i==0:
            diag+=dim*dim+increment
        else:
            diag+=increment
        if isprime(diag):
            prime_count+=1
        diagonals.append(diag)
    ratio=prime_count/len(diagonals)
    if ratio<2/15:
        break
    dim+=2
    k+=1
ratio=3*ratio/4
print(dim)
stop=timeit.default_timer()
print("Runtime:",stop-start)
