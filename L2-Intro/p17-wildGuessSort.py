import p15_insertionSort as insertionSort

def wildGuessSort(A):
    for i in range(0, len(A)):
        if A[i] > A[i+1]:
            return insertionSort.insertionSort(A)
        else:
            return A

def test1():
    arr = [int(digit) for digit in str(529501233)]
    print(arr)
    print(wildGuessSort(arr))

if __name__ == "__main__":
    test1()