import pickle
import os
import queue


def isprime(i):
    for j in range(2,round(i/2)+1):
        if(i%j==0):
            return False
    return True


if "primes" not in os.listdir():
    primes=[2]
    for i in range(1,int(pow(10,6)/2)+1):
        if isprime(2*i+1):
            primes.append(2*i+1)
    pickle.dump(primes,open("primes","wb"))
else:
    primes=pickle.load(open("primes","rb"))


i=0
sum=0
min_len=0
max_len=0
limit=pow(10,6)
traversal=[]
while True:
    sum+=primes[i]
    if sum>=limit:
        sum-=primes[i]
        max_len=len(traversal)
        break
    traversal.append(primes[i])
    if isprime(sum) and min_len<len(traversal):
        max_sum=sum
        min_len=len(traversal)
    i+=1

traversal=queue.Queue()
flag=0
for j in range(max_len-min_len):
    sum=0
    k=max_len-j
    for i in range(k):
        traversal.put(primes[i])
        sum+=primes[i]

    while sum<limit:
        if isprime(sum):
            flag=1
            break
        i+=1
        sum=sum-traversal.get()+primes[i]
        traversal.put(primes[i])

    if flag:
        max_sum=sum
        min_len=k
        break

    while traversal.empty()==False:
        traversal.get()

print("The longest sum of consecutive primes below", limit,
      "that adds to a prime, contains", min_len, "terms, and is"
      " equal to", max_sum)
