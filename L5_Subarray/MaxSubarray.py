from math import inf

# return the maxsubarray value where the starting time can equal to ending.
def MaxSubarray(A, p, r):
    if p == r:
        return A[p]
    q = p + (r - p) // 2
    m1 = MaxSubarray(A, p, q)
    m2 = MaxSubarray(A, q + 1, r)
    Lmax, Rmax = -inf, -inf
    v = 0
    for i in range(q, p - 1, -1):
        v += A[i]
        if v > Lmax:
            Lmax = v
    v = 0
    for i in range(q + 1, r + 1):
        v += A[i]
        if v > Rmax:
            Rmax = v
    return max(m1, m2, Lmax + Rmax)

# return the maxsubarray index
def maxSubarrayIdx(A, p, r):
    if p == r:
        return A[p], p, r
    q = p + (r-p) // 2
    m1, a, b = maxSubarrayIdx(A, p, q)
    m2, c, d = maxSubarrayIdx(A, q+1, r)
    Lmax, Rmax = -inf, -inf
    v = 0
    for i in range(q, p - 1, -1):
        v += A[i]
        if v > Lmax:
            Lmax = v
            e = i
    v = 0
    for i in range(q + 1, r + 1):
        v += A[i]
        if v > Rmax:
            Rmax = v
            f = i
    maxA = max(m1, m2, Lmax + Rmax)
    if maxA == m1:
        return m1, a, b
    if maxA == m2:
        return m2, c, d
    return Lmax+Rmax, e, f

# return the maxSubarray such that starting index != ending index
def MaxSubarray2(A, p, r):
    if p == r:
        return 0
    if p == r - 1:
        if A[p] > A[r]:
            return 0
        else: 
            return A[r] - A[p]
    q = p + (r - p) // 2
    m1 = MaxSubarray2(A, p, q)
    m2 = MaxSubarray2(A, q + 1, r)
    Lmax, Rmax = -inf, -inf
    v = 0
    for i in range(q, p - 1, -1):
        v += A[i]
        if v > Lmax:
            Lmax = v
    v = 0
    for i in range(q + 1, r + 1):
        v += A[i]
        if v > Rmax:
            Rmax = v
    return max(m1, m2, Lmax + Rmax)

# def maxSubarrayIdx2(A, p, r):
#     if p == r:
#         return -inf, p, r
#     if p == r - 1:
#         if A[p] > A[r]:
#             return -inf, p, r
#         else: 
#             return A[r] - A[p], p, r
#     q = p + (r-p) // 2
#     m1, a, b = maxSubarrayIdx(A, p, q)
#     m2, c, d = maxSubarrayIdx(A, q+1, r)
#     Lmax, Rmax = -inf, -inf
#     v = 0
#     for i in range(q, p - 1, -1):
#         v += A[i]
#         if v > Lmax:
#             Lmax = v
#             e = i
#     v = 0
#     for i in range(q + 1, r + 1):
#         v += A[i]
#         if v > Rmax:
#             Rmax = v
#             f = i
#     maxA = max(m1, m2, Lmax + Rmax)
#     if maxA == m1:
#         return m1, a, b
#     if maxA == m2:
#         return m2, c, d
#     return Lmax+Rmax, e, f

if __name__ == "__main__":
    A = [1, -2, 3, -4, -5]
    print(MaxSubarray(A, 0, len(A) - 1))
    print(MaxSubarray2(A, 0, len(A) - 1))
    print(maxSubarrayIdx(A, 0, len(A) - 1))
    # print(maxSubarrayIdx2(A, 0, len(A) - 1))