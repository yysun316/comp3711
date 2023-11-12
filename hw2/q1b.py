def rangeSum(A, C):
    for i in range(len(C)):
        sum = 0
        for j in range(len(A)):
            if A[j] <= i + 1:
                sum += A[j]
        C[i] = sum
    
def sum(x,y,C):
    return C[y] - C[x]


if __name__ == "__main__":
    A = [2, 3, 4, 4, 4, 5, 8, 6]
    C = [0 for _ in range(0, 9)]
    rangeSum(A, C)
    print(C)
    print(sum(3-1, 6-1, C))