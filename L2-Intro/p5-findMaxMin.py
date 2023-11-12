#find the max and min in an array
# Takes 2n-2 comparisions which is bad, so we should improve it to 
def findMaxMin(arr):
    max = arr[0]
    min = arr[0]
    max_pos = -1
    min_pos = -1
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
            max_pos = i
        # if arr[i] < min: bad because it increaes the number of comparisions
        elif arr[i] < min: # better
            min = arr[i]
            min_pos = i
    return [max_pos, max, min_pos, min]

def test1():
    arr = [int(digit) for digit in str(529501233)]
    print(arr)
    print(findMaxMin(arr))

if __name__ == '__main__':
    test1()