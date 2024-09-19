from time import time
from copy import deepcopy

start = time()
triangle = open("data.txt",  "r")
matrix = []
line = triangle.readline()
while line:
    line = line.rstrip("\n")
    line = line.split(" ")
    matrix.append(line)
    line = triangle.readline()

matrix = [list(map(int, row)) for row in matrix]
row_num = len(matrix)
id_matrix = deepcopy(matrix)
identifier = 0
for i in range(len(id_matrix)):
    for j in range(i+1):
        id_matrix[i][j] = identifier
        identifier += 1

path_map = {}
identifier = 0
for i in range(len(matrix)):
    for j in range(i+1):
        path_map[(id_matrix[i][j])] = matrix[i][j]

child = []
children = {}
for i in range(len(matrix)):
    for j in range(i+1):
        dummy = [-1, -1]
        if i < len(matrix)-1:
            child.append(id_matrix[i+1][j])
            child.append(id_matrix[i+1][j+1])
            dummy = deepcopy(child)
        children[id_matrix[i][j]] = dummy
        child.clear()

mid_elements = []
for i in range(len(id_matrix)):
    for j in range(i+1):
        if j != 0 and j != i:
            mid_elements.append(id_matrix[i][j])


total = 0
temp = matrix[0][0]
identifier = 0
traverse = [identifier]
aborted = []
j = 0
while True:
    tag = 0
    for k in range(2):
        for dumped in aborted:
            if dumped == children[identifier][k]:
                tag += 1
    if tag == 2:
        for dude in mid_elements:
            if dude == aborted[len(aborted)-1]:
                aborted.pop()
        j = (j+1) % 2
        junk = traverse.pop()
        temp -= path_map.get(junk)
        aborted.append(junk)
        if len(traverse) == 0:
            break
        identifier = traverse[len(traverse) - 1]
        continue
    child = children[identifier][j]
    traverse.append(child)
    temp += path_map.get(child)
    if children[child][j] != -1:
        identifier = child
    else:
        if total < temp:
            total = temp
        junk = traverse.pop()
        temp -= path_map.get(junk)
        aborted.append(junk)
        identifier = traverse[len(traverse) - 1]
        j = (j+1) % 2
print(total)
end = time()
print('Time elapsed', end - start, 'seconds')
