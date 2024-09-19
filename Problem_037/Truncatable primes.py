import pickle
import os

scale=4
def istruncatable_bothside(n):
    number=str(n)
    while len(number)>1:
        number=number[1:]
        if int(number) not in primes:
            return False
    number=str(n)
    while len(number)>1:
        number=number[:-1]
        if int(number) not in primes:
            return False
    return True

def calculateprimes(k):

    for i in range(k*pow(10,scale),(k+1)*pow(10,scale)):
        count=0
        for j in range(1,round(i/2)+1):
            if(i%j==0):
                count+=1
            if(count>1):
                break
        if(count==1):
            primes.append(i)
    pickle.dump(primes,open("primes","wb"))

primes=[]
t_primes=[]


sum=0
k=0
flag=0
while True:
    if "primes" not in os.listdir():
        calculateprimes(k)
        print("Primes calculated till", k*pow(10,scale))
        k+=1
    else:
        primes=pickle.load(open("primes","rb"))
        for prime in primes:
            if prime > (k-1)*pow(10,scale):
                if(prime<10):
                    continue
                if istruncatable_bothside(prime):
                    t_primes.append(prime)
                    sum+=prime
                    #print(prime)
                    if len(t_primes)==11:
                        flag=1
                        break
    if flag:
        break

print(sum)
