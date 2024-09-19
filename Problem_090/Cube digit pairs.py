from time import time
from itertools import combinations
from copy import deepcopy


def upside_down(dice):
    if 6 in dice and 9 not in dice:
        dice.append(9)
    elif 9 in dice and 6 not in dice:
        dice.append(6)
    return dice


def check_cubes(cube1, cube2):
    if not {0, 1, 2, 3, 4, 5, 6, 8, 9}.issubset(set(cube1 + cube2)):
        return False
    check = deepcopy(target)
    for value1 in cube1:
        for value2 in cube2:
            number = str(value1) + str(value2)
            if number in check:
                check.remove(number)
                if not check:
                    return True
            number = str(value2) + str(value1)
            if number in check:
                check.remove(number)
                if not check:
                    return True
    return False


start = time()
num_set = []
target = []
solution = 0
for i in range(0, 10):
    if i:
        target.append(str(i*i))
        if len(target[-1]) == 1:
            target[-1] = "0" + target[-1]
    num_set.append(i)
all_combs = list(combinations(num_set, 6))
for i in range(0, len(all_combs)):
    dice1 = list(all_combs[i])
    dice1x = upside_down(deepcopy(dice1))
    for j in range(i+1, len(all_combs)):
        dice2 = list(all_combs[j])
        dice2x = upside_down(deepcopy(dice2))
        if check_cubes(dice1x, dice2x):
            solution += 1
print(solution)

end = time()
print("Time elapsed", end-start, "seconds")
