import networkx as nx
import matplotlib.pyplot as plt
import random

k = 0


def create_graph(n):
    g = nx.DiGraph()
    node_num = n
    for i in range(node_num):
        g.add_node(i)
    for i in range(random.randint(node_num, node_num * 2)):
        while True:
            start = random.randint(0, node_num - 1)
            end = random.randint(0, node_num - 1)
            if (not start == end) and (not g.has_edge(start, end)):
                if start > end:
                    start, end = end, start
                g.add_edge(start, end)
                break
    nx.draw(g, with_labels=True)
    plt.savefig("pic2_1.png")
    plt.show()
    return g


def dfs(l, node):
    neighbors = list(graph.neighbors(node))
    global k
    if len(neighbors) == 0:
        if l > k:
            k = l
            print(k)
        return
    else:
        for i in neighbors:
            dfs(l + 1, i)


def divide_k():
    # 建立indegree数组
    inDegree = [0]*node_number
    edges = graph.edges()
    for sn, en in edges:
        inDegree[en] += 1
    group = [[] for _ in range(k+1)]
    for i in graph.nodes():
        if inDegree[i] == 0:
            group[0].append(i)
    for i in range(k):
        for j in group[i]:
            neighbors = list(graph.neighbors(j))
            for neighbor in neighbors:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    group[i+1].append(neighbor)
    for i in range(k+1):
        print(group[i])


if __name__ == '__main__':
    node_number = 10
    graph = create_graph(node_number)
    marked = [False] * node_number
    for nn in range(node_number):
        if not marked[nn]:
            dfs(0, nn)
    print(k)
    print(graph.nodes())
    divide_k()
