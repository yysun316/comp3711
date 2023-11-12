from math import inf


def find_largest_set(A):
    S = set()

    while A.count(None) < len(A):
        largest_index = 0
        largest = -inf
        for i in range(len(A)):
            if A[i] is not None and A[i] > largest:
                largest = A[i]
                largest_index = i
        S.add(largest)
        # Mark largest and its neighbor as deleted
        A[largest_index] = None
        if largest_index - 1 >= 0:
            A[largest_index - 1] = None

        if largest_index + 1 < len(A):
            A[largest_index + 1] = None

    return S


A = [1,4,6,4]
largest_set = find_largest_set(A)
print("Largest set:", largest_set)
