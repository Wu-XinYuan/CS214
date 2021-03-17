def qsort2(start, end, a, b):
    # 终止条件，待筛选的队列为空
    if start >= end:
        return
    s = start
    e = end
    pos = 0
    # 寻找与b[s]相对的a[pos]
    for i in range(s, e + 1):
        if a[i] == b[s]:
            pos = i
            break
    # 交换a[pos]的位置到第一个
    a[s], a[pos] = a[pos], a[s]
    while True:
        while (a[e] >= b[start]) and s < e:
            e = e - 1
        if s < e:
            a[s] = a[e]
            s = s + 1
        while (a[s] <= b[start]) and s < e:
            s = s + 1
        if s < e:
            a[e] = a[s]
            e = e - 1
        if s >= e:
            break
    a[s] = b[start]
    pos = s
    s = start
    e = end
    while True:
        while (b[e] >= a[pos]) and s < e:
            e = e - 1
        if s < e:
            b[s] = b[e]
            s = s + 1
        while (b[s] <= a[pos]) and s < e:
            s = s + 1
        if s < e:
            b[e] = b[s]
            e = e - 1
        if s >= e:
            break
    b[s] = a[pos]
    qsort2(start, s-1, a, b)
    qsort2(s+1, end, a, b)


if __name__ == '__main__':
    bolt = [3, 11, 5, 2, 6, 9, 4, 10, 8, 1, 7]
    nut = [2, 4, 9, 10, 7, 6, 3, 1, 11, 5, 8]
    qsort2(0, len(bolt)-1, bolt, nut)
    print(bolt)
    print(nut)
