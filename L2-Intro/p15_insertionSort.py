def insertionSort(A):
    for i in range(1, len(A)):
        j = i - 1
        while A[j] > A[j+1] and j >= 0:
            # swap
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp
            j -= 1
    return A

def test1():
    arr = [int(digit) for digit in str(529501233)]
    print(arr)
    print(insertionSort(arr))

if __name__ == "__main__":
    test1()