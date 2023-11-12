def merge(A, p, q, r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    L.append(float("inf"))
    R.append(float("inf"))
    i = j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergeSort(A, p, r):
    if p >= r:
        return
    q = (p+r)//2
    mergeSort(A, p, q)
    mergeSort(A, q+1, r)
    merge(A, p, q, r)

if __name__ == "__main__":
    A = [5, 2, 4, 7, 1, 2, 6, 3]
    mergeSort(A, 0, len(A)-1)
    print(A)