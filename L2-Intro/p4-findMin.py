# finding minimum in array {pos, val}

def findMin(arr):
    min = arr[0]
    pos = -1
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            pos = i
    return [pos, min]

def test1():
    arr = [int(digit) for digit in str(529501233)]
    print(arr)
    print(findMin(arr))

if __name__ == '__main__':
    test1()