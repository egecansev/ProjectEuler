import time


start = time.time()
guttus = []
guttus.append(2)
for i in range(1, 34):
    for j in range(3):
        if j == 1:
            guttus.append(2 * i)
        else:
            guttus.append(1)
num =guttus.pop(0)
den = 1
sum = 0
for i in guttus:
    num, den = den, num
    num = i * den + num
target = str(num)
number = list(target)
while number:
    sum += int(number.pop())
end = time.time()
print(sum)
print("Time elapsed is ", end - start, " seconds")

