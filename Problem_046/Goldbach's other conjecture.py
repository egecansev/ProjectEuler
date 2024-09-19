import pickle
from math import sqrt


def isprime(i):
    for j in range(2,round(i/2)+1):
        if(i%j==0):
            return False
    return True


def isnotprime(i):
    for j in range(2,round(i/2)+1):
        if(i%j==0):
            return True
    return False


n=1
while True:
    flag=0
    i=1
    count=0
    if isnotprime(n):
        while(n>2*i*i+1):
            if isprime(n-2*i*i):
                flag=0
                break
            else:
                flag=1
                count+=1
            i+=1
        if flag:
            print(n)
            break
    n+=2
