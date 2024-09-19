from time import time


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        self.depth = 0


def add_child(n, child):
    if child.data in depth_map.keys():
        if n.depth + 1 <= depth_map[child.data]:
            n.children.append(child)
            child.parent = n
            child.depth = child.parent.depth + 1
            nodes.append(child)
            depth_map[child.data] = child.depth


def get_grandparents(n, gp):
    if not n.parent:
        return gp
    parent = n.parent
    gp.append(parent)
    get_grandparents(parent, gp)
    return gp


start = time()
limit = 200
depth_map = {}
for i in range(2, limit + 1):
    depth_map[i] = 100
undone = list(range(2, limit + 1))
root = Node(1)
nodes = [root]
for node in nodes:
    family = get_grandparents(node, [node])
    for dude in family:
        baby = node.data + dude.data
        add_child(node, Node(baby))
        if baby in undone:
            undone.remove(baby)
    if not undone:
        break
print(sum(depth_map.values()))
end = time()
print('Time elapsed', end - start, 'seconds')
