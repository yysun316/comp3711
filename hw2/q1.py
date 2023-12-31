def rangeQueryMin(C, a, i, j):
    if i == j:
        # if a < C[i] and i > 0:
        #     return i - 1
        if a > C[i] and i < len(C) - 1:
            return i + 1
        else:
            return i
    m = (i + j) // 2
    if a <= C[m]:
        return rangeQueryMin(C, a, i, m - 1)
    else:
        return rangeQueryMin(C, a, m + 1, j)


def rangeQueryMax(C, b, i, j):
    if i == j:
        # if b > C[i] and i < len(C) - 1:
        #     return i + 1
        if b < C[i] and i > 0:
            return i - 1
        else:
            return i
    m = (i + j) // 2
    if b < C[m]:  # finding the 1st element that is larger than b
        return rangeQueryMax(C, b, i, m - 1)
    else:
        return rangeQueryMax(C, b, m + 1, j)


def printRange(C, a, b):
    max = rangeQueryMax(C, b, 0, len(C) - 1)
    min = rangeQueryMin(C, a + 1, 0, len(C) - 1)
    print(max)
    print(min)
    # if the indexes are equal, then we need to check if the value is within the range
    if max == min:
        # if C[max] > a and C[min] <= b:
        if a < C[min] and C[min] <= b:
            print(1)
        else:
            print(0)
    else:
        print(max - min + 1)
    print("\n")


# general test cases
# 1. a is not found and b is found
def test1():
    c = [2, 3, 4, 4, 4, 5, 6, 8]
    a = 3  
    b = 6  
    # [4, 6] max = 6, min = 2 -> 6-2+1 = 5
    printRange(c, a, b)  # 5


# 2. a is found and b is out of range
def test2():
    c = [2, 3, 4, 4, 4, 5, 6, 8]
    a = 7
    b = 10
    # [8, 10] max = 7, min = 7
    printRange(c, a, b)  # 1


# a is out of range and b is found
def test3():
    c = [1, 3, 5]
    a = -1
    b = 5
    # [0, 5] max = 2, min = 0
    printRange(c, a, b)  # 3


# a is not found and b is not found
def test4():
    c = [1, 3, 5]
    a = -1
    b = 6
    # [0, 6] max = 2, min = 0
    printRange(c, a, b)  # 3


# a is found and b is found
def test5():
    c = [1, 3, 5]
    a = 0
    b = 3
    # [1, 3] max = 1, min = 0
    printRange(c, a, b)  # 2


def test6():
    c = [1, 3, 3, 3, 3, 5, 5, 5, 5, 6] 
    a = 2
    b = 5
    # [3,5] max = 9, min = 0
    printRange(c, a, b)  # 8


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
