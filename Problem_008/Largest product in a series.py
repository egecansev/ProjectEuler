from time import time

start = time()
series = open("the number.txt", "r")
line = series.readline()
number = ""
while line:
    line = line.rstrip("\n")
    number = number+line
    line = series.readline()
multiplicand = 0
for i in range(len(number)-12):
    temp = 1
    for j in range(13):
        temp *= int(number[i+j])
    if temp > multiplicand:
        multiplicand = temp
print(multiplicand)
end = time()
print('Time elapsed', end - start, 'seconds')
