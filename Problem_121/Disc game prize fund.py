from time import time
from itertools import combinations

start = time()
turns = 15
prob_blue = []
prob_red = []
for i in range(2, turns + 2):
    prob_blue.append(1 / i)
    prob_red.append(1 - 1 / i)
blue = turns
all_indexes = range(turns)
total_probability = 0
while blue > turns / 2:
    blue_indexes = combinations(all_indexes, blue)
    for indexes in blue_indexes:
        probability = 1
        for index in all_indexes:
            if index in indexes:
                probability *= prob_blue[index]
            else:
                probability *= prob_red[index]
        total_probability += probability
    blue -= 1
print(int(1 // total_probability))
end = time()
print('Time elapsed', end - start, 'seconds')
