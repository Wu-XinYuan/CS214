import networkx as nx
import matplotlib.pyplot as plt
import random


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
    # 保证所有点的度数都是偶数
    node1 = -1
    for i in range(node_num):
        if len(g[i]) % 2 == 0:
            continue
        if node1 == -1:
            node1 = i
        else:
            if g.has_edge(node1, i):
                g.remove_edge(node1, i)
            else:
                g.add_edge(node1, i)
            node1 = -1
    return g


# graph为每边都为偶数的无向图，n为graph中结点的个数，节点编号为0-n-1
def mark(graph):
    dgraph = nx.DiGraph()  # 创建有向图，用于存放标记好的边
    # for i in graph.nodes:
    #     dgraph.add_node(i)
    # 开始遍历
    for i in graph.nodes:
        while len(graph[i]) > 0:
            neighbors = list(graph.neighbors(i))
            j = neighbors[0]
            s, e = i, j
            while True:
                dgraph.add_edge(s, e)
                graph.remove_edge(s, e)
                s = e
                if s == i:
                    break
                neighbors_e = list(graph.neighbors(s))
                e = neighbors_e[0]
    return dgraph


if __name__ == '__main__':
    node_number = 10
    graph_raw = create_graph(node_number)
    print(list(graph_raw.edges))
    nx.draw(graph_raw, with_labels=True)
    plt.savefig("graph_raw.png")
    plt.show()
    graph_d = mark(graph_raw)
    nx.draw(graph_d, with_labels=True)
    plt.savefig("graph_d.png")
    plt.show()
