def insert(A, x, i):
    A[i] = x # insert x into the last position of A
    while i > 0 and A[i] < A[i//2]: # if the child is smaller, swap
        A[i], A[i//2] = A[i//2], A[i]
        i = i//2

def extractMin(heap):
    if len(heap) == 0:
        return None

    # Store the minimum value (root of the min-heap)
    min_value = heap[0]

    # Move the last element to the root
    heap[0] = heap[-1]
    heap.pop()

    # Bubble down the root to restore the min-heap property
    parent_index = 0
    while True:
        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2

        # Find the index of the smallest child
        smallest_child_index = parent_index

        if left_child_index < len(heap) and heap[left_child_index] < heap[smallest_child_index]:
            smallest_child_index = left_child_index

        if right_child_index < len(heap) and heap[right_child_index] < heap[smallest_child_index]:
            smallest_child_index = right_child_index

        # If the smallest child is smaller than the parent, swap them
        if smallest_child_index != parent_index:
            heap[parent_index], heap[smallest_child_index] = heap[smallest_child_index], heap[parent_index]
            parent_index = smallest_child_index
        else:
            break

    return min_value

def heapSort(A):
    n = len(A)
    # build a min heap
    for i in range(0, n):
        insert(A, A[i], i)
    # extract min n times
    for i in range(n-1, -1, -1):
        A[i] = extractMin(A, i+1)

if __name__ == "__main__":
    A = [5, 2, 4, 7, 1, 2, 6, 3]
    heapSort(A)
    print(A)