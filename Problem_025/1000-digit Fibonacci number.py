fibo=[]
for i in range(2):
    fibo.append(1)
limit=pow(10,999)
i=0
while(1):
    fibo.append(fibo[i]+fibo[i+1])
    i+=1
    if(fibo[len(fibo)-1]>limit):
        break
print(len(fibo))
