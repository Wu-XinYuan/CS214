def count_times(A, B, next):
    i, j = 0, 0
    cnt = 0
    len_a, len_b = len(A), len(B)
    while i < len_a:
        if j == len(B):
            cnt = cnt + 1
            j = next[len_b - 1] + 1
        if B[j] == A[i]:
            i, j = i+1, j+1
        else:
            j = next[j]
            if j == -1:
                i, j = i+1, 0
    if j == len(B):
        cnt = cnt + 1
    return cnt


def get_next(B):
    next = []
    next.append(-1)
    next.append(0)
    for i in range(2, len(B)):
        j = next[i-1] + 1
        while (b[i-1] != b[j-1] and j >= 0):
            j = next[j-1]
        next.append(j)
    #print('next: {}'.format(next))
    return next


if __name__ == '__main__':
    while True:
        a = input("input string A:")
        b = input("input string B:")
        next = get_next(b)
        print("B appears {} times in A".format(count_times(a, b, next)))

