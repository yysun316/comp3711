def findMaxMin(arr):
    max = arr[0]
    min = arr[0]
    max_pos = -1
    min_pos = -1
    for i in range(1, len(arr)- 1, 2): # step = 2
        if arr[i] > arr[i+1]:
            if arr[i] > max:
                max = arr[i]
                max_pos = i
            if arr[i+1] < min:
                min = arr[i+1]
                min_pos = i+1
        else: 
            if arr[i+1] > max:
                max = arr[i+1]
                max_pos = i+1
            if arr[i] < min:
                min = arr[i]
                min_pos = i
    return [max_pos, max, min_pos, min]

def test1():
    arr = [int(digit) for digit in str(529501233)]
    print(arr)
    print(findMaxMin(arr))

if __name__ == '__main__':
    test1()

