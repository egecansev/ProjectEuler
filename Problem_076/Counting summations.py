import numpy as np
from time import time


def pent_gen(n):
    pents = {}
    for x in range(n+1):
        pents[int((3*x*x-x)/2)] = x
        if x:
            pents[int((3 * x * x + x) / 2)] = -x
    return pents


def inv_mat(n):
    if n in pentagonals.keys():
        m = pentagonals.get(n)
        element = -(-1)**(m+1)
    else:
        element = 0
    return element


start = time()
number = 101
matrix = np.zeros(shape=(number, number))
pentagonals = pent_gen(number)
j = 0
for i in range(number):
    for k in range(i, number):
        matrix[k-i+j][i] = inv_mat(k-i)
    j += 1
print(int(np.linalg.inv(matrix)[-1][0]-1))
end = time()
print('Time elapsed', end - start, 'seconds')
