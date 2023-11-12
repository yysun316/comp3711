def merge_and_count(A, p, q, r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    i = j = c = 0
    k = p

    while i < q - p + 1 and j < r - q:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            c += q - p + 1 - i
        k += 1

    while i < q - p + 1:
        A[k] = L[i]
        k += 1
        i += 1

    while j < r - q:
        A[k] = R[j]
        k += 1
        j += 1

    return c

def sort_and_count(A, p, r):
    if p == r:
        return 0
    q = p + (r-p)//2
    c1 = sort_and_count(A, p, q)
    c2 = sort_and_count(A, q+1, r)
    c3 = merge_and_count(A, p, q, r)
    return c1 + c2 + c3

if __name__ == "__main__":
    A = [3,2,1,0]
    print(sort_and_count(A, 0, len(A) - 1))