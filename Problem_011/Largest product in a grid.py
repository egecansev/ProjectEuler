from time import time


def combo(i, j, elements):
    down = 1
    right = 1
    diagonal = 1
    off_diagonal = 1
    for k in range(4):
        if i < 17:
            down *= int(elements[i+k][j])
        else:
            down = -1
        if j < 17:
            right *= int(elements[i][j+k])
        else:
            right = -1
        if i < 17 and j < 17:
            diagonal *= int(elements[i+k][j+k])
        else:
            diagonal = -1
        if i > 2 and j < 17:
            off_diagonal *= int(elements[i-k][j+k])
        else:
            off_diagonal = -1
    return max(down, right, diagonal, off_diagonal)


start = time()
grid = open("the matrix", "r")
matrix = []
line = grid.readline()
while line:
    line = line.rstrip()
    line = line.split(" ")
    matrix.append(line)
    line = grid.readline()
multiplicand = 0
for a in range(20):
    for b in range(20):
        temp = combo(a, b, matrix)
        if temp > multiplicand:
            multiplicand = temp
print(multiplicand)
end = time()
print('Time elapsed', end - start, 'seconds')
