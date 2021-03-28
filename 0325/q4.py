def manacher(str_old):
    str_m = []
    for i in range(len(str_old)):
        str_m.append(-1)
        str_m.append(ord(str_old[i]))
    str_m.append(-1)
    radius = []
    c, r = -1, -1  # c代表中心位置，r代表当前最长子串右边界
    max_len = 0
    for i in range(len(str_m)):
        if r > i:  # i在当前最长字串内
            radius.append(min(radius[2*c-i], r-i+1))  # 对称位置回文长度，或者到右边界的距离
        else:
            radius.append(1)
        while i + radius[i] < len(str_m) and i - radius[i] >= 0:
            if str_m[i - radius[i]] == str_m[i+radius[i]]:
                radius[i] += 1
            else:
                break
        if i + radius[i] > r:
            r = i + radius[i] -1
            c = i
        if radius[i] > max_len:
            max_len = radius[i]
    return max_len - 1


if __name__ == '__main__':
    string = input("input the string: ")
    print(manacher(string))
