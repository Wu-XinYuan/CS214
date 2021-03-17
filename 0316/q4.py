def find_reverse(array, start, end):
    if start >= end:
        return 0
    mid = int((start + end) / 2)
    sum_l = find_reverse(array, start, mid)  # 左子串的逆序对数
    sum_r = find_reverse(array, mid + 1, end)  # 右子串的逆序对数

    # 求新产生的逆序对数，并归并成有序队列
    sum_n = 0
    p_l, p_r, p_n = start, mid + 1, start  # 指向待归并的数和待存入的位置
    n_r = 0  # 记录右侧子序列中已被归并的个数，则当前归并的左边子串中的数会产生n_r个逆序对
    array_t = array[start:end + 1]  # 存储待归并的数组
    while (p_l <= mid) and (p_r <= end):
        if array_t[p_l - start] < array_t[p_r - start]:
            array[p_n] = array_t[p_l - start]
            p_l, p_n = p_l + 1, p_n + 1
            sum_n = sum_n + n_r
        else:
            array[p_n] = array_t[p_r - start]
            p_r, p_n = p_r + 1, p_n + 1
            n_r = n_r + 1
    # 左边字串若没归并完继续填充
    if p_l <= mid:
        array[p_n:end + 1] = array_t[p_l - start: mid + 1 - start]
        sum_n = sum_n + n_r * (mid - p_l + 1)
    # 若右子串没归并完直接填充
    if p_r <= end:
        array[p_n:end + 1] = array_t[p_r - start: end + 1 - start]
    return sum_l + sum_r + sum_n


if __name__ == '__main__':
    a = [9, 8, 7, 6, 5, 4]  # 定义待求逆序对数的数组
    print(find_reverse(a, 0, len(a) - 1))
