from math import sqrt
from itertools import combinations


def fact (n):
    mult=1
    for i in range(2,n+1):
        mult*=i
    return mult


def comb(n,r):
    return fact(n)/(fact(r)*fact(n-r))


def isprime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True


primes=[]
digits=[]
index_set=[]
i=10
target=8
while True:
    flag1=0
    i+=1
    if isprime(i)==False:
        continue
    length=len(str(i))-1
    digits.clear()
    index_set.clear()
    for k in range(length):
        digits.append(k)
    for j in range(1,length+1):
        for item in combinations(digits,j):
            index_set.append(list(item))
    for m in index_set:
        number=str(i)
        if m[0]:
            for x in range(10):
                for n in m:
                    number=number[:n]+str(x)+number[n+1:]
                if isprime(int(number)):
                    primes.append(number)
            if len(primes)==target:
                flag1=1
                break
            primes.clear()
        else:
            for x in range(1,10):
                for n in m:
                    number=number[:n]+str(x)+number[n+1:]
                if isprime(int(number)):
                    primes.append(number)
            if len(primes)==target:
                flag1=1
                break
            primes.clear()
    if flag1:
        break


print(int(primes[0]))
