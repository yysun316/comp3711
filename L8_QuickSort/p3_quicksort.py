def partition(A, p, r):
    x = A[r] # select the last element as pivot
    i = p - 1 # i is the index of the last element in the left half
    for j in range(p, r): # j is the index of the current element
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i] # swap A[i] and A[j]
    A[i+1], A[r] = A[r], A[i+1] # swap A[i+1] and A[r]
    return i+1 # return the pivot index
# O(n) time
def quickSort(A, p, r):
    if p >= r: # if starting index >= ending index, return
        return
    # All items <= pivot are moved to left of pivot
    q = partition(A, p, r) # q is the pivot index
    quickSort(A, p, q-1) # sort the left half
    quickSort(A, q+1, r) # sort the right half
# O(nlogn) time

if __name__ == "__main__":
    A = [5, 2, 4, 7, 1, 2, 6, 3]
    quickSort(A, 0, len(A)-1)
    print(A)


# [5, 2, 4, 7, 1, 2, 6, 3] pivot = 3
# [2, 2, 1, 3, 5, 4, 7, 6] pivot = 6

# O(n^2) worst case 
# O(nlogn) average case
# T(n) = 2T(n/2) + O(n)
