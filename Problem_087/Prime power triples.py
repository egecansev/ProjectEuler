from time import time
from sympy import primerange


def take_closest(mylist, mynumber):

    mylist.append(mynumber)
    mylist.sort()
    indx = mylist.index(mynumber)
    mylist.remove(mynumber)
    return indx


start = time()

numbers = []
limit = 50 * 10 ** 6
set_x = list(primerange(1, int((limit - 2 ** 3 - 2 ** 4) ** (1 / 2)) + 1))
set_y = list(primerange(1, int((limit - 2 ** 2 - 2 ** 4) ** (1 / 3)) + 1))
set_z = list(primerange(1, int((limit - 2 ** 2 - 2 ** 3) ** (1 / 4)) + 1))

for z in set_z:
    for y in set_y:
        remainder = limit - y ** 3 - z ** 4
        if remainder < 0:
            break
        close_x = remainder ** 0.5
        solution = take_closest(set_x, close_x)
        for i in range(solution):
            numbers.append(set_x[i] ** 2 + y ** 3 + z ** 4)
unique_numbers = set(numbers)
print(len(unique_numbers))

end = time()
print('Time elapsed', end - start, 'seconds')
