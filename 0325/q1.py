def find_lcs(str1, str2):
    max_len = 0
    lcs = [[0 for y in range(len(str2)+1)] for x in range(len(str1)+1)]  # 初始化为全0
    print(lcs)
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            print("i:{} j:{}".format(i, j))
            if str1[i-1] == str2[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
                if lcs[i][j] > max_len:
                    max_len = lcs[i][j]
                continue
            if lcs[i-1][j] > lcs[i][j-1]:
                lcs[i][j] = lcs[i-1][j]
            else:
                lcs[i][j] = lcs[i][j-1]
    print(lcs)
    return lcs[len(str1)][len(str2)]


if __name__ == '__main__':
    while True:
        stringT = input("input string T:")
        stringP = input("input string P:")
        length_lcs = find_lcs(stringT, stringP)
        print("length of LCS:{}".format(length_lcs))
        print("length of SCS:{}".format(len(stringP)+len(stringT)-length_lcs))
