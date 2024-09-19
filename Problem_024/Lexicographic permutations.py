from random import shuffle
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i;
    return fact


numbers=[]
for i in range(10):
    numbers.append(i)

value=pow(10,6)-1
lex_perm=""
while(len(numbers)):
    for i in range(1,11):
        if(factorial(i)>value):
            res=i-1
            break
    order=int(value/factorial(res))
    chosen=numbers[order]
    value-=order*factorial(res)
    numbers.remove(chosen)
    chosen=str(chosen);
    lex_perm+=chosen
print(lex_perm)



