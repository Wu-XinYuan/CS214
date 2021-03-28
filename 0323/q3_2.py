def percolate_down(array, length, hole):
    child = hole * 2
    tmp = array[hole]
    while child <= length:
        if child < length:
            if array[child + 1] > array[child]:
                child += 1
        if array[child] > tmp:
            array[hole] = array[child]
            hole = child
            child *= 2
        else:
            break
    array[hole] = tmp


def heap_sort(array, length, k):
    # 建堆
    for i in range(int(length/2), 0, -1):
        percolate_down(array, length, i)
    # 出堆k次
    output = []
    for i in range(k):
        output.append(array[1])
        array[1] = array[length]
        length -= 1
        percolate_down(array, length, 1)
    return output


if __name__ == '__main__':
    while True:
        input_array = input("input array A:")
        input_array = [int(n) for n in input_array.split()]
        input_array.insert(0, 0)  # 插入首位，使计算时数组从1开始
        input_i = int(input("input i:"))
        print(heap_sort(input_array, len(input_array)-1, input_i))
