sum=0
for i in range(1,1001):
    sum+=pow(i,i)
sum=str(sum)
answer=""
for i in range(len(sum)-10,len(sum)):
    answer+=sum[i]
print(answer)
