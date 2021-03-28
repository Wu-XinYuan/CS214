def count_sort(array, k):
    length = len(array)
    if length < 2:
        return array
    max_num = max(array)
    min_num = min(array)
    diff = max_num - min_num
    count = [0] * (diff + 1)
    for element in array:
        count[element - min_num] += 1
    output = []
    for i in range(diff, -1, -1):
        while count[i] > 0 and k > 0:
            output.append(i + min_num)
            count[i] -= 1
            k -= 1
        if k == 0:
            break
    return output


if __name__ == '__main__':
    while True:
        a = input("input array A:")
        a = [int(n) for n in a.split()]
        i = int(input("input i:"))
        print(count_sort(a, i))
