from time import time

start = time()
number = pow(2, 1000)
total = 0
number = str(number)
for i in range(len(number)):
    total += int(number[i])
print(total)
end = time()
print('Time elapsed', end - start, 'seconds')
