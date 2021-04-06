import random


def make_binary_tree(d):
    t = [0, 1]
    # print(2**3)
    for i in range(2, 2**d):
        if t[int(i/2)] == 0:
            t.append(0)
        else:
            t.append(int(random.randint(0, 2) > 0))
    for i in range(1, d+1):
        for j in range(2**(i-1), 2**i):
            print(t[j], end=' ')
        print()
    return t


def find_leaf(t, d):
    # for i in range(2**d, 2**(d+1)):
    #     t.append(0)
    for i in range(1, d):
        for j in range(2**(i-1), 2**i):
            if t[j*2] == 0 and t[j*2+1] == 0:
                return i-1
    return d-1


if __name__ == '__main__':
    depth = 4
    tree = make_binary_tree(depth)
    print(find_leaf(tree, depth))
