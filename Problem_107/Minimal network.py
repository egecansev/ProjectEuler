from time import time
from numpy import nonzero, min, zeros, array
from urllib import request


def update_subtrees(subtrees, i, j):
    first = -1
    second = -1
    for subtree in subtrees:
        if i in subtree:
            first = subtrees.index(subtree)
        if j in subtree:
            second = subtrees.index(subtree)

    if first == -1 and second == -1:
        subtrees.append([i, j])
    elif first == -1 and second != -1:
        subtrees[second].append(i)
    elif first != -1 and second == -1:
        subtrees[first].append(j)
    elif first > second:
        subtrees.append(subtrees.pop(first) + subtrees.pop(second))
    elif first < second:
        subtrees.append(subtrees.pop(second) + subtrees.pop(first))
    else:
        return False
    return True


def Kruskal(matrix):
    mst = zeros(shape=(len(matrix), len(matrix)))
    subtrees = []
    while True:
        min_weight = min(matrix[nonzero(matrix)])
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == min_weight:
                    if update_subtrees(subtrees, i, j):
                        mst[i][j] = matrix[i][j]
                        mst[j][i] = matrix[j][i]
                        if len(subtrees) == 1 and len(subtrees[0]) == len(matrix):
                            return sum(sum(mst)) / 2
                    matrix[i][j] = 0
                    matrix[j][i] = 0


start = time()
network = []
data = request.urlopen("https://projecteuler.net/project/resources/p107_network.txt")
for line in data:
    network.append(list(map(int, line.decode("utf-8").rstrip("\n").replace("-", "0").split(','))))
network = array(network)
initial_weight = sum(sum(network)) / 2
print(int(initial_weight - Kruskal(network)))
end = time()
print('Time elapsed', end - start, 'seconds')
