import pickle
import os

primes=[]
if "primes" not in os.listdir():
    for i in range(1,100000):
        count=0
        for j in range(1,round(i/2)+1):
            if(i%j==0):
                count+=1
            if(count>1):
                break
        if(count==1):
            primes.append(i)
            print(i)
    pickle.dump(primes,open("primes","wb"))

else:
    primes=pickle.load(open("primes","rb"))

max_series=0
for i in range(-999,1000):
    for j in range(-999,1000):
        cnt=0
        for n in range (1000):
            number=n*n+i*n+j
            if number in primes:
                cnt+=1
            else:
                break
        temp=cnt
        if(max_series<temp):
            product=i*j
            a=i
            b=j
            max_series=temp

print(product)
