def digit_sum(n):
    num=list(str(n))
    sum=0
    for i in num:
        sum+=int(i)
    return sum

max_digit_sum=0
for a in range(1,100):
    for b in range(1,100):
        sum=digit_sum(pow(a,b))
        if max_digit_sum<sum:
            max_digit_sum=sum
print(max_digit_sum)
