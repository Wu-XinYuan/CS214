import networkx as nx
import matplotlib.pyplot as plt
import random


dfs_n = 0
stack = []


def create_graph(n):
    g = nx.Graph()
    node_num = n
    for i in range(node_num):
        g.add_node(i)
    for i in range(random.randint(node_num, node_num*2)):
        while True:
            start = random.randint(0, node_num-1)
            end = random.randint(0, node_num-1)
            if (not start == end) and (not g.has_edge(start, end)):
                g.add_edge(start, end)
                break
    return g


# 包裹bc函数
def bc_wrap(n1, n2, n3, n4):
    for n in graph.nodes():
        graph.nodes[n]['dfs_num'] = 0
    global dfs_n
    dfs_n = len(graph.nodes())
    bc(-1, 0)
    # 如果两条边在一个连通支内，返回真
    for n in graph.nodes:
        print(graph.nodes[n]['group'], graph.nodes[n]['high'])
    return graph.nodes[n1]['group'] == graph.nodes[n2]['group'] == graph.nodes[n3]['group'] == graph.nodes[n4]['group']


def bc(parent, node):
    # 有问题，应该把边放进去
    global stack, dfs_n
    graph.nodes[node]['dfs_num'] = dfs_n
    dfs_n -= 1
    stack.append(node)
    print(stack)
    graph.nodes[node]['high'] = graph.nodes[node]['dfs_num']
    neighbors = list(graph.neighbors(node))
    for neighbor in neighbors:
        if neighbor == parent:
            continue
        if graph.nodes[neighbor]['dfs_num'] == 0:
            bc(node, neighbor)
            if graph.nodes[neighbor]['high'] <= graph.nodes[node]['dfs_num']:
                node_m = -1
                while node_m != node:
                    node_m = stack[len(stack)-1]
                    stack.remove(node_m)
                    graph.nodes[node_m]['group'] = node
                stack.append(node)
            graph.nodes[node]['high'] = max(graph.nodes[node]['high'], graph.nodes[neighbor]['high'])
        else:
            graph.nodes[node]['high'] = max(graph.nodes[node]['high'], graph.nodes[neighbor]['dfs_num'])


if __name__ == '__main__':
    node_number = 10
    graph = create_graph(node_number)
    a = random.randint(0, len(graph.edges()))
    b = random.randint(0, len(graph.edges()))
    while a == b:
        b = random.randint(0, len(graph.edges()))
    c = random.randint(0, len(graph.edges()))
    while a == c or b == c:
        c = random.randint(0, len(graph.edges()))
    edges = list(graph.edges())
    graph.remove_edge(edges[c][0], edges[c][1])
    nx.draw(graph, with_labels=True)
    plt.savefig("pic3_1.png")
    plt.show()
    print(edges[a][0], edges[a][1], edges[b][0], edges[b][1], edges[c][0], edges[c][1])
    print(bc_wrap(edges[a][0], edges[a][1], edges[b][0], edges[b][1]))
