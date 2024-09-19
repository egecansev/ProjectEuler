def isprime(n):
    for i in range(2,int(n/2)+1):
        if(n%i==0):
            return False
    return True


def primefactors (n,k):
    count=0
    for i in range(2,int(n/2)+1):
        if(n%i==0):
            if isprime(i):
                count+=1
        if count==k:
            return True
    return False

pf=4
i=1
while True:
    k=i
    for j in range(pf):
        if primefactors(k,pf):
            k+=1
        else:
            break
    if k==i+pf:
        print(i)
        break
    i+=1
