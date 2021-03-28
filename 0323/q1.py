import math

def find_min_k(array1, array2, k, start, end):
    print('k:{} start:{} end:{}'.format(k, start, end))
    if start == end:
        if array1[start] > array2[k - start]:
            return array1[start]
        else:
            return array2[k - start]
    mid = int((start + end + 1) / 2)
    if array1[mid] > array2[k - mid + 1]:
        return find_min_k(array1, array2, k, start, mid - 1)
    else:
        return find_min_k(array1, array2, k, mid, end)


if __name__ == '__main__':
    while True:
        a = input("input array A:")
        a = [int(n) for n in a.split()]
        b = input("input array B:")
        b = [int(n) for n in b.split()]
        k = int(input("input k:"))
        len_a, len_b = len(a), len(b)
        a.insert(0, a[0] - 1)
        b.insert(0, b[0] - 1)
        a.append(a[len_a] + 1)
        b.append(b[len_b] + 1)
        #print('a:{}'.format(a))
        #print('b:{}'.format(b))
        e = min(k, len_a)
        s = max(1, k - len_b)
        print("the k-th number is:{}".format(find_min_k(a, b, k, s, e)))

