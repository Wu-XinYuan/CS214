import random


def reachable(table, sx, sy, ex, ey):
    min_cross = [[-1] * (width + 2) for _ in range(height + 2)]
    can_reach = [[False] * (width + 2) for _ in range(height + 2)]
    directions = [[[0, 0, 0, 0]] * (width + 2) for _ in range(height + 2)]  # 四个方向依次为上下左右
    # 将起始位置放入队首
    queue = [[sx, sy]]
    can_reach[sx][sy] = True
    while len(queue) != 0:
        x, y = queue[0]
        queue.remove(queue[0])
        cross = min_cross[x][y] + 1
        # 转弯次数超过两个，不判断
        if cross == 3:
            continue
        # 向四个方向拓展：
        for t in range(4):
            if directions[x][y][t] == 1:  # 是从这个方向来的，那这个方向一定已经遍历过
                continue
            if t == 0:
                nx, ny = x, y - 1
            elif t == 1:
                nx, ny = x, y + 1
            elif t == 2:
                nx, ny = x-1, y
            else:
                nx, ny = x+1, y
            while 0 <= nx <= width + 1 and 0 <= ny <= height + 1 and table[nx][ny] == 0:
                directions[nx][ny][t] = 1
                if not can_reach[nx][ny]:
                    queue.append([nx, ny])
                    can_reach[nx][ny] = True
                    min_cross[nx][ny] = cross
                if t == 0:
                    ny -= 1
                elif t == 1:
                    ny += 1
                elif t == 2:
                    nx -= 1
                else:
                    nx += 1
            if 0 <= nx <= width + 1 and 0 <= ny <= height + 1:
                min_cross[nx][ny] = cross
    if min_cross[ex][ey] == -1:
        return False
    else:
        return True


if __name__ == '__main__':
    width, height = 3, 3
    blocks = [[0] * (width + 2) for _ in range(height + 2)]
    for i in range(1, width + 1):
        for j in range(1, height + 1):
            blocks[i][j] = random.randint(0, 1)
    startx = random.randint(1, width)
    starty = random.randint(1, height)
    endx = random.randint(1, width)
    endy = random.randint(1, height)
    while startx == endx and starty == endy:
        endx = random.randint(1, width)
        endy = random.randint(1, height)
    blocks[startx][starty] = 1
    blocks[endx][endy] = 1
    for i in range(len(blocks)):
        for j in range(len(blocks)):
            print(blocks[i][j], end='\t')
        print()
    print("start:{},{} end:{},{}".format(startx, starty, endx, endy))
    print(reachable(blocks, startx, starty, endx, endy))
