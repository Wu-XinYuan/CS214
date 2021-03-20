def find_max(s, e, a):
    if s == e:
        return a[s]
    mid = int((s + e) / 2)
    max_l = find_max(s, mid, a)
    max_r = find_max(mid+1, e, a)
    if max_l > max_r:
        return max_l
    else:
        return max_r


def find_min(s, e, a):
    if s == e:
        return a[s]
    mid = int((s + e) / 2)
    min_l = find_min(s, mid, a)
    min_r = find_min(mid+1, e, a)
    if min_l < min_r:
        return min_l
    else:
        return min_r


if __name__ == '__main__':
    array = input("input array A:")
    array = [int(n) for n in array.split()]
    print("max: %d \t min: %d" % (find_max(0, len(array)-1, array), find_min(0, len(array)-1, array)))
