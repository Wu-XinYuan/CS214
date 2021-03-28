from q4_1 import qsort


def find3(array, sum_i):
    qsort(array, 0, len(array) - 1)
    for i in range(len(array) - 2):
        s = i + 1
        e = len(array) - 1
        sum2 = sum_i - array[i]
        while s < e:
            while s < e and array[s] + array[e] > sum2:
                e -= 1
            if s < e and array[s] + array[e] == sum2:
                print(array[i], array[s], array[e])
                return True
            while s < e and array[s] + array[e] < sum2:
                s += 1
            if s < e and array[s] + array[e] == sum2:
                print(array[i], array[s], array[e])
                return True
    return False


if __name__ == '__main__':
    while True:
        input_array = input("input array A:")
        input_array = [int(n) for n in input_array.split()]
        input_sum = int(input("input sum:"))
        print(find3(input_array, input_sum))
