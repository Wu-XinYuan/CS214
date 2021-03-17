import math

def findsqrt(minval, maxval, x):
    print("%d, %d, %d" % (minval, maxval, x))
    if minval == maxval:
        return minval
    mid = math.floor((minval + maxval) / 2)
    mids = mid * mid
    midn = (mid + 1) * (mid + 1)
    print("%d, %d" % (mid, mids))
    if (mids <= x) and (midn > x):
        return mid
    if mids > x:
        return findsqrt(minval, mid - 1, x)
    else:
        return findsqrt(mid + 1, maxval, x)


if __name__ == '__main__':
    while True:
        num = int(input("input number, or input a negative number to end: "))
        if num < 0:
            break
        else:
            print(findsqrt(0, num, num))
