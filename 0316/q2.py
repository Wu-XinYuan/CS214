def findz(start, end, a, z):
    if a[start] == z:
        return start
    if a[end] == z:
        return end
    mid = int((start + end) / 2)
    if a[mid] == z:
        return mid
    if a[mid] > z:
        return findz(start + (z - a[start]), mid - 1, a, z)
    else:
        return findz(mid + 1, end - (a[end] - z), a, z)


if __name__ == '__main__':
    array = input("input array A:")
    array = [int(n) for n in array.split()]
    print(array)
    num = int(input("input z:"))
    print("the position is %d" % (findz(0, len(array)-1, array, num)+1))
