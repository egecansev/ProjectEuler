n=1
power=1
count=0
new_count=1
while new_count!=0:
    new_count=0
    i=1
    while len(str(n))<=power:
        n=pow(i,power)
        if len(str(n))==power:
            new_count+=1
        i+=1
    count+=new_count
    power+=1
print(count)
