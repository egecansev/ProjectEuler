def factorial (num):
    mult=1
    for i in range(1,num+1):
        mult*=i
    return mult


def combination (a,b):
    comb=factorial(a)/(factorial(b)*factorial(a-b))
    return comb

target=pow(10,6)
count=0
for n in range(1,101):
    cnt=0
    if factorial(n)>target:
        for r in range(n):
            if combination(n,r)>target:
                count+=1

print(count)
