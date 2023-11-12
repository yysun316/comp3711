# Selection Sort
def selectionSort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                # swap
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr


def test1():
    arr = [int(digit) for digit in str(529501233)]
    print(arr)
    print(selectionSort(arr))


if __name__ == "__main__":
    test1()
