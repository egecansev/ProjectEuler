import timeit


start=timeit.default_timer()
num = [3, 7]
den = [2, 5]
while len(num) != 1000:
    new_num = 2 * num[-1] + num[-2]
    new_den = den[-1] + num[-1]
    num.append(new_num)
    den.append(new_den)
count = 0
for i in range(0, 1000):
    if len(str(num[i])) > len(str(den[i])):
        count += 1
print(count)
stop=timeit.default_timer()
print("Runtime:",stop-start)