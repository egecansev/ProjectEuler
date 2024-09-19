import networkx as nx
import time


def gen_ser(k):
    n = 1
    x = 0
    tri = []
    sqr = []
    penta = []
    hexa = []
    hepta = []
    octa = []
    series=[tri,sqr,penta,hexa,hepta,octa]
    for i in range(6):
        while len(str(x))<5:
            if i == 0:
                x=int(n*(n+1)/2)
                if len(str(x)) == 4 and int(str(x)[2]):
                    tri.append(x)
            elif i == 1:
                x=int(n*n)
                if len(str(x)) == 4 and int(str(x)[2]):
                    sqr.append(x)
            elif i == 2:
                x=int(n*(3*n-1)/2)
                if len(str(x))==4 and int(str(x)[2]):
                    penta.append(x)
            elif i == 3:
                x = int(n * (2 * n - 1))
                if len(str(x)) == 4 and int(str(x)[2]):
                    hexa.append(x)
            elif i == 4:
                x=int(n*(5*n-3)/2)
                if len(str(x))==4 and int(str(x)[2]):
                    hepta.append(x)
            elif i == 5:
                x=int(n*(3*n-2))
                if len(str(x))==4 and int(str(x)[2]):
                    octa.append(x)
            n+=1
        n=1
        x=0
    return series[:k]


def gen_graph(series):
    k = len(series)
    Graph = nx.DiGraph()
    for i in range(k):
        for element in series[i]:
            j = (i + 1) % k
            while j != i:
                for candidate in series[j]:
                    if str(element)[-2:] == str(candidate)[:2]:
                        Graph.add_edge(element,candidate)
                j = (j + 1) % k
    return Graph


def check_series (series, candidate):
    relationship = {}
    for node in candidate:
        dummy = []
        for i in range(len(series)):
            if node in series[i]:
                dummy.append(i)
        relationship[node] = dummy
    classes = sorted(relationship.values(), key=len)
    dummy = []
    for i in range(len(series)):
        dummy.append(i)
    for serie in classes:
        if len(serie) == 1:
            if serie[0] in dummy:
                dummy.remove(serie[0])
            else:
                return False
        else:
            if len(dummy) <= len(serie):
                for element in dummy:
                    if element not in serie:
                        return False
    return True


if __name__=="__main__":
    start = time.time()

    length = 6
    serseries=gen_ser(length)
    G = gen_graph(serseries)

    while True:
        nodes = []
        cycle = nx.find_cycle(G)
        for edge in cycle:
            for node in edge:
                if node not in nodes:
                    nodes.append(node)
        if len(nodes) == length:
            if check_series(serseries, nodes):
                break
        G.remove_edges_from(cycle)
        # while len(nodes):
        #     node = nodes.pop()
        #     G.remove_node(node)

    sum = 0
    print(nodes)
    for node in nodes:
        sum = sum + node
    print(sum)
    end = time.time()
    print("Time elapsed is ", end- start, " seconds.")