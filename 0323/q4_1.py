def qsort(array, start, end):
    if start >= end:
        return
    tmp = array[start]
    s, e = start, end
    while True:
        while array[e] >= tmp and s < e:
            e -= 1
        if s < e:
            array[s] = array[e]
            s += 1
        while array[s] <= tmp and s < e:
            s += 1
        if s < e:
            array[e] = array[s]
            e -= 1
        if s == e:
            break
    array[s] = tmp
    qsort(array, start, s-1)
    qsort(array, s+1, end)


def find2(array, sum_i):
    qsort(array, 0, len(array) - 1)
    s = 0
    e = len(array) - 1
    while s < e:
        while s < e and array[s] + array[e] > sum_i:
            e -= 1
        if s < e and array[s] + array[e] == sum_i:
            print(array[s], array[e])
            return True
        while s < e and array[s] + array[e] < sum_i:
            s += 1
        if s < e and array[s] + array[e] == sum_i:
            print(array[s], array[e])
            return True
    return False


if __name__ == '__main__':
    while True:
        input_array = input("input array A:")
        input_array = [int(n) for n in input_array.split()]
        input_sum = int(input("input sum:"))
        print(find2(input_array, input_sum))
