from time import time


def divisors_sum(n):
    sum = 0
    for i in range(1, round(n/2)+1):
        if n % i == 0:
            sum += i
    return sum


start = time()
abundant=[]
sum=0
limit=28123
for i in range(1,limit+1):
    sum+=i
    if(i<divisors_sum(i)):
        abundant.append(i)

abundant_sum=[]
flag=0
for i in range(len(abundant)-1):
    for j in range(len(abundant)-1):
        sum_abundant=abundant[i]+abundant[j]
        if(sum_abundant<limit+1):
            abundant_sum.append(sum_abundant)
        else:
            break

abundant_sum=set(abundant_sum)

while (len(abundant_sum)):
    sum-=abundant_sum.pop()

print(sum)
end = time()
print('Time elapsed', end - start, 'seconds')