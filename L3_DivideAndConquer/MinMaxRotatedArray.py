# MinMaxRotatedArray.py
# Distinct elements
def findMin(A, p, r):
    if p >= r:
        return A[p] # only 1 element, it's the min
    mid = p + (r-p)//2
    if A[mid] > A[r]:
        return findMin(A, mid+1, r)
    else:
        return findMin(A, p, mid) # mid can be the min, so include it
    
def find_min(A):
    if len(A) == 1:
        return A[0]
    left, right = 0, len(A) - 1
    while left < right: # cannot be equal, otherwise infinite loop
        mid = left + (right - left) // 2
        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid # mid can be the min, so include it
    return A[left]
    
def findMax(A, p, r):
    if p == r:
        return A[p]
    mid = p + (r-p)//2
    if A[mid] > A[p]:
        return findMax(A, mid, r)
    else:
        return findMax(A, p, mid)
    
def find_max(A):
    if len(A) == 1:
        return A[0]
    left, right = 0, len(A) - 1
    while left < right:
        mid = left + (right - left) // 2
        if A[mid] > A[left]:
            left = mid
        else:
            right = mid
    return A[left]

# Non-distinct elements

def find_min2(A):
    if len(A) == 1:
        return A[0]
    left, right = 0, len(A) - 1
    while left < right:
        mid = left + (right - left) // 2
        if A[mid] > A[right]:
            left = mid + 1
        elif A[mid] < A[right]:
            right = mid
        else:
            right -= 1
    return A[left]

def find_max2(A):
    if len(A) == 1:
        return A[0]
    left, right = 0, len(A) - 1
    while left < right:
        mid = left + (right - left) // 2
        if A[mid] > A[left]:
            left = mid
        elif A[mid] < A[left]:
            right = mid
        else:
            left += 1
    return A[left]


if __name__ == "__main__":
    A = [4,5,6,7,9,10,12,0,1,2,3]
    B = [2,2,2,3,0,1]
    print(findMin(A, 0, len(A)-1))
    print(find_min(A))
    print(findMax(A, 0, len(A)-1))
    print(find_max(A))
    print(find_min2(B))
    print(find_max2(B))











# [4 5 6 7 0 1 2]
# mid > right -> min is in right half
