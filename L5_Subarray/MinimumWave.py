def MinWave(A, p, r):
    if p == r:
        return A[p]
    q = p + (r - p) // 2
    if A[q - 1] > A[q] and A[q + 1] > A[q]:
        return A[q]
    if A[q] > A[q + 1] or A[q] > 0:
        return MinWave(A, q + 1, r)
    else:
        return MinWave(A, p, q - 1)


if __name__ == "__main__":
    A = [0, 2, 5, 8, 4, 3, 1, -3, -5, -2, 0]
    print(MinWave(A, 0, len(A) - 1))
