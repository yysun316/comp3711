def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def selection1(A, p, r, i):
    if p == r:
        return A[p]
    q = partition(A, p, r)
    k = q - p + 1 # calculate the relative position of the pivot
    if i == k:
        return A[q]
    elif i < k:
        return selection1(A, p, q - 1, i)
    else:
        return selection1(A, q + 1, r, i - k)

def selection2(A, p, r, i): # wrong.
    if p == r:
        return A[p]
    q = partition(A, p, r)
    if i == q:
        return A[q]
    elif i < q:
        return selection2(A, p, q-1, i)
    else:
        return selection2(A, q + 1, r, i)
    
if __name__ == "__main__":
    A = [1,2,3,4,5,6,7,8,9]
    print(selection1(A, 0, len(A)-1, 6))
    print(selection2(A, 0, len(A)-1, 6))