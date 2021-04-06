import networkx as nx
import matplotlib.pyplot as plt
import random


def create_tree(n):
    global root
    g = nx.Graph()
    node_num = n
    for i in range(node_num):
        g.add_node(i)
    nodes_out = list(g.nodes)
    root = random.randint(0, node_num-1)
    nodes_in = [root]
    nodes_out.remove(root)
    while len(nodes_out) > 0:
        e = nodes_out[random.randint(0, len(nodes_out)-1)]
        s = nodes_in[random.randint(0, len(nodes_in))-1]
        g.add_edge(s, e)
        nodes_out.remove(e)
        nodes_in.append(e)
    nx.draw(g, with_labels=True)
    plt.savefig("pic4_1.png")
    plt.show()
    return g


def dfs(parent, node):
    neighbors = list(tree.neighbors(node))
    for neighbor in neighbors:
        if neighbor == parent:
            continue
        dfs(node, neighbor)
        b[node] += max(a[neighbor], b[neighbor])
    for neighbor in neighbors:
        if neighbor == parent:
            continue
        # 尝试将i和neighbor加入匹配，看能否构成最大匹配
        a[node] = max(a[node], b[node] - max(a[neighbor], b[neighbor]) + b[neighbor] + 1)
    print(node)
    print(a)
    print(b)


if __name__ == '__main__':
    node_number = 10
    root = 0
    tree = create_tree(node_number)
    a = [0]*node_number
    b = [0]*node_number
    dfs(-1, root)
    print(max(a[root], b[root]))
