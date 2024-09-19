from time import time

start = time()
data = open("data.txt", "r")
line = data.readline()
total = 0
while line:
    total += int(line.rstrip("\n"))
    line = data.readline()
print(int(str(total)[:10]))
end = time()
print('Time elapsed', end - start, 'seconds')
