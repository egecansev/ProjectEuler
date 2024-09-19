import itertools

digit=[]
for i in range (10):
    digit.append(str(i))
pandigital=list(itertools.permutations(digit,len(digit)))
for i in range(len(pandigital)):
    pandigital[i]="".join(pandigital[i])

primes=[]
for i in range(2,18):
    primes.append(i)
    for j in range(2,i):
        if(i%j==0):
            primes.pop()
            break

sum=0
for number in pandigital:
    flag=1
    i=1
    for prime in primes:
        if int(number[i:i+3])%prime!=0:
            flag=0
            break
        i+=1
    if flag:
        sum+=int(number)

print(sum)
