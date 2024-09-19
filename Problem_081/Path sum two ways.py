#   Dijkstra's Algorithm is used


from time import time
from urllib import request


def merge(item):
    for char in item:
        if type(char) != str:
            item.insert(item.index(char), str(char))
            item.remove(char)
    return item[0] + ',' + item[1]


def right_neighbour(n):
    index = [int(n[0]), int(n[1]) + 1]
    value = matrix[index[0]][index[1]]
    name = merge(index)
    return [name, value]


def bottom_neighbour(n):
    index = [int(n[0]) + 1, int(n[1])]
    value = matrix[index[0]][index[1]]
    name = merge(index)
    return [name, value]


start = time()
data = request.urlopen("https://projecteuler.net/project/resources/p081_matrix.txt")
matrix = []
for line in data:
    line = str(line)[2:-3].split(',')
    matrix.append(list(map(int, line)))


nodes = []
for row in matrix:
    index_row = str(matrix.index(row))
    for i in range(len(row)):
        index_column = str(i)
        nodes.append(merge([index_row, index_column]))
distances = {}
for node in nodes:
    node = node.split(',')
    if int(node[0]) != len(matrix)-1 and int(node[1]) != len(matrix)-1:
        right = right_neighbour(node)
        bottom = bottom_neighbour(node)
        node = merge(node)
        distances.update({node: {right[0]: right[1], bottom[0]: bottom[1]}})
    elif int(node[0]) == len(matrix)-1 and int(node[1]) != len(matrix)-1:
        right = right_neighbour(node)
        node = merge(node)
        distances.update({node: {right[0]: right[1]}})
    elif int(node[0]) != len(matrix) - 1 and int(node[1]) == len(matrix) - 1:
        bottom = bottom_neighbour(node)
        node = merge(node)
        distances.update({node: {bottom[0]: bottom[1]}})
    else:
        node = merge(node)
        distances.update({node: {}})


unvisited = {node: None for node in nodes}  # using None as +inf
visited = {}
current = '0,0'
currentDistance = matrix[0][0]
end = str(len(matrix)-1) + ',' + str(len(matrix)-1)
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited:
            continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited:
        break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]
print(visited.popitem()[1])

end = time()
print("Time elapsed", end - start, "seconds")
