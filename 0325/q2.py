def twenty_four(layer):
    if layer == 4:
        if array[3][0] == 24:
            print(array)
        return array[3][0] == 24
    for i1 in range(4-layer):
        for i2 in range(5-layer):
            if i1 == i2:
                continue
            num1 = array[layer-1][i1]
            num2 = array[layer-1][i2]
            if num1 < num2:
                num1, num2 = num2, num1
            i4 = 1  # 将上一层没有用到的数保存到这一层，i3指向这种数在上一层的位置，i4指向在这一层将被保留的位置
            for i3 in range(5 - layer):
                if i3 != i1 and i3 != i2:
                    array[layer][i4] = array[layer-1][i3]
                    i4 += 1
            array[layer][0] = num1 + num2
            if twenty_four(layer + 1):
                return True
            array[layer][0] = num1 - num2
            if twenty_four(layer + 1):
                return True
            array[layer][0] = num1 * num2
            if twenty_four(layer + 1):
                return True
            if num2 != 0:
                array[layer][0] = num1 / num2
                if twenty_four(layer + 1):
                    return True
    return False


if __name__ == '__main__':
    array = [[0]*4 for _ in range(5)]
    while True:
        input_array = input("input array A:")
        input_array = [int(n) for n in input_array.split()]
        for i in range(4):
            array[0][i] = input_array[i]
        print(twenty_four(1))
