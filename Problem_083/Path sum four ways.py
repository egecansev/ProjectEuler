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


def top_neighbour(n):
    index = [int(n[0]) - 1, int(n[1])]
    value = matrix[index[0]][index[1]]
    name = merge(index)
    return [name, value]


def left_neighbour(n):
    index = [int(n[0]), int(n[1]) - 1]
    value = matrix[index[0]][index[1]]
    name = merge(index)
    return [name, value]


def check_position(n):
    for char in n:
        if type(char) != int:
            n.insert(n.index(char), int(char))
            n.remove(char)
    if n[0] == 0:
        if n[1] == 0:
            return 'top_left'
        elif n[1] == len(matrix) - 1:
            return 'top_right'
        else:
            return 'top'
    elif n[0] == len(matrix) - 1:
        if n[1] == 0:
            return 'bottom_left'
        elif n[1] == len(matrix) - 1:
            return 'bottom_right'
        else:
            return 'bottom'
    elif n[1] == 0:
        return 'left'
    elif n[1] == len(matrix) - 1:
        return 'right'
    else:
        return 'middle'


start = time()
data = request.urlopen("https://projecteuler.net/project/resources/p083_matrix.txt")
matrix = []
password = ''
for line in data:
    line = str(line)[2:-3].split(',')
    matrix.append(list(map(int, line)))

# matrix = [
#     [131, 673, 234, 103, 18],
#     [201, 96, 342, 965, 150],
#     [630, 803, 746, 422, 111],
#     [537, 699, 497, 121, 956],
#     [805, 732, 524, 37, 331]]

nodes = []
for row in matrix:
    index_row = str(matrix.index(row))
    for i in range(len(row)):
        index_column = str(i)
        nodes.append(merge([index_row, index_column]))
distances = {}
for node in nodes:
    node = node.split(',')
    node_position = check_position(node)
    if node_position == 'top_right':
        left = left_neighbour(node)
        bottom = bottom_neighbour(node)
        neighbours = left, bottom
    elif node_position == 'top_left':
        right = right_neighbour(node)
        bottom = bottom_neighbour(node)
        neighbours = right, bottom
    elif node_position == 'bottom_left':
        right = right_neighbour(node)
        top = top_neighbour(node)
        neighbours = right, top
    elif node_position == 'left':
        right = right_neighbour(node)
        bottom = bottom_neighbour(node)
        top = top_neighbour(node)
        neighbours = right, bottom, top
    elif node_position == 'right':
        left = left_neighbour(node)
        bottom = bottom_neighbour(node)
        top = top_neighbour(node)
        neighbours = left, bottom, top
    elif node_position == 'top':
        right = right_neighbour(node)
        left = left_neighbour(node)
        bottom = bottom_neighbour(node)
        neighbours = right, left, bottom
    elif node_position == 'bottom':
        right = right_neighbour(node)
        left = left_neighbour(node)
        top = top_neighbour(node)
        neighbours = right, left, top
    elif node_position == 'middle':
        right = right_neighbour(node)
        left = left_neighbour(node)
        bottom = bottom_neighbour(node)
        top = top_neighbour(node)
        neighbours = right, left, bottom, top
    else:
        neighbours = [[None, None]]

    node = merge(node)
    # distances.update({node: {right[0]: right[1], bottom[0]: bottom[1]}})
    distances.update({node: {element[0]: element[1] for element in neighbours}})



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
    if current == end:
        break
    if not unvisited:
        break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]
print(visited.popitem()[1])
end = time()
print("Time elapsed", end - start, "seconds")
