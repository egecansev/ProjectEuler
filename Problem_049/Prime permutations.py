from itertools import permutations
from math import sqrt

def isprime(n):
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return False
    return True

pperm=[]
visited=[]
results=[]
number=""
for i in range(500,5000):
    if i not in visited and 2*i+1!=1487:
        pperm.clear()
        flag1=0
        flag2=0
        if isprime(2*i+1):
            lisa=list(str(2*i+1))
            lisa=list(permutations(lisa,4))
            for lis in lisa:
                lis="".join(lis)
                if int(lis)%2 and int(lis)>1000:
                    if int(lis) not in visited:
                        visited.append(int(lis))
                    if isprime(int(lis)) and lis not in pperm:
                        pperm.append(lis)
            if len(pperm)>2:
                pperm=sorted(pperm)
                for m in range(len(pperm)):
                    if int(pperm[m])==1487:
                        continue
                    for n in range(m+1,len(pperm)):
                        inc=int(pperm[n])-int(pperm[m])
                        if str(int(pperm[n])+inc) in pperm:
                            for f in range(3):
                                number+=str(2*i+1 + f*inc);
                            if len(number)==12:
                                results.append(int(number))
                            number=""
                            flag2=1
                            break
                    if flag2:
                        break
print(results.pop())
