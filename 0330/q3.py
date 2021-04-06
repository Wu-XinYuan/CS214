import networkx as nx
import matplotlib.pyplot as plt
import random


def create_graph(n):
    g = nx.Graph()
    node_num = n
    for i in range(node_num):
        g.add_node(i)
    for i in range(random.randint(node_num, node_num * 2)):
        while True:
            start = random.randint(0, node_num - 1)
            end = random.randint(0, node_num - 1)
            if (not start == end) and (not g.has_edge(start, end)):
                g.add_edge(start, end)
                break
    # 保证是连通的
    for i in g.nodes:
        if len(g[i]) == 0:
            if i > n / 2:
                end = random.randint(0, i - 1)
            else:
                end = random.randint(i + 1, node_num - 1)
            g.add_edge(i, end)
    return g


def find_point(g):
    graph = g.copy()
    for n in graph.nodes:
        graph.nodes[n]['marked'] = False
    node = 0
    flag = True
    while flag:
        graph.nodes[node]['marked'] = True
        neighbors = graph.neighbors(node)
        flag = False
        # 在node的临点中寻找未被标记过的，如果都已经被标记过了，就说明是叶子结点
        for neighbor in neighbors:
            if not graph.nodes[neighbor]['marked']:
                flag = True
                node = neighbor
                break
    return node


if __name__ == '__main__':
    node_number = 10
    graph_i = create_graph(node_number)
    nx.draw(graph_i, with_labels=True)
    plt.savefig("pic3_1.png")
    plt.show()
    node_del = find_point(graph_i)
    print(node_del)
    graph_i.remove_node(node_del)
    nx.draw(graph_i, with_labels=True)
    plt.savefig("pic3_2.png")
    plt.show()
