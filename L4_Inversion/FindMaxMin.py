def findMinMax(A, p ,r):
    if p == r:
        return A[p], A[p]
    if r == p+1:
        if A[p] > A[r]:
            return A[p], A[r]
        else:
            return A[r], A[p]
    q = p + (r-p) // 2
    maxL, minL = findMinMax(A, p, q)
    maxR, minR = findMinMax(A, q+1, r)
    if maxL > maxR:
        maxA = maxL
    else:
        maxA = maxR
    if minL < minR:
        minA = minL
    else:
        minA = minR
    return maxA, minA

if __name__ == "__main__":
    A = [1, 10, 3, 5, 9]
    print(findMinMax(A, 0, len(A)-1))
# returns a tuple