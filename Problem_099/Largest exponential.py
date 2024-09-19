from time import time
from math import log
from urllib import request


start = time()
maximum = 0
index = 1
max_index = 1
data = request.urlopen("https://projecteuler.net/project/resources/p099_base_exp.txt")
for line in data:
    line = line.decode("utf-8").split(',')
    value = int(line[1]) * log(int(line[0]))
    if value > maximum:
        maximum = value
        max_index = index
    index += 1
print(max_index)
end = time()
print('Time elapsed', end - start, 'seconds')
