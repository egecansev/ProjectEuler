import copy
def factorial(n):
    prod=1
    for i in range(1,n+1):
        prod*=i
    return prod

curious_sum=0
number=3
numb=copy.deepcopy(number)
numb=str(numb)
while(len(numb)*factorial(9)>=number):
    sum=0
    for i in range(len(numb)):
        sum+=factorial(int(numb[i]))
    if(number==sum):
        curious_sum+=number
        print(number)
    number+=1
    numb=copy.deepcopy(number)
    numb=str(numb)
print(curious_sum)

