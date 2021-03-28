import random


# 用于生成成绩矩阵
def generate_grade():
    for i in range(n - 1):
        for j in range(i + 1, n):
            grade[i][j] = 2 * random.randint(0, 1) - 1  # 1或-1
            grade[j][i] = - grade[i][j]
    for i in range(len(grade)):
        for j in range(len(grade[i])):
            print(grade[i][j], end='\t')
        print()


'''
得出符合要求的序列，
输入为二维数组grade, 人数n
grade[i][j]为1时代表i打败了j,否则为-1
'''
def find_queue():
    queue = [0]
    for i in range(1, n):
        if grade[i][queue[0]] == 1:  # 打败了队首，放队首
            queue.insert(0, i)
            continue
        if grade[i][queue[i - 1]] == -1:  # 被队尾打败，放队尾
            queue.append(i)
            continue
        pos = find_pos(i, 0, i-2, queue)  # 要插入在第pos个后面
        queue.insert(pos+1, i)
    return queue


# 找到一个满足grade[i][queue[pos]]=-1且grade[i][queue[pos+1]]=1的位置
def find_pos(i, start, end, queue):
    if start == end:
        return start
    mid = int((start + end + 1) / 2)
    if grade[i][queue[mid]] == -1 and grade[i][queue[mid + 1]] == 1:
        return mid
    if grade[i][queue[mid]] == 1:
        return find_pos(i, start, mid - 1, queue)
    else:
        return find_pos(i, mid, end, queue)


if __name__ == '__main__':
    n = 10
    grade = [[0] * n for _ in range(n)]
    generate_grade()
    print(find_queue())
