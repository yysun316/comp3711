# Python3 Program to find kth element from two sorted arrays. Time Complexity: O(log k)
def kth(arr1, m, arr2, n, k):
	if (k > (m + n) or k < 1):
		return -1
	# # Let m <= n
	# if (m > n):
	# 	return kth(arr2, n, arr1, m, k)
	# Check if arr1 is empty returning k-th element of arr2
	if (m == 0):
		return arr2[k - 1]
	# Check if k = 1 return minimum of first two elements of both arrays
	if (k == 1):
		return min(arr1[0], arr2[0])
	# Now the divide and conquer part
	i = min(m, k // 2)
	j = min(n, k // 2)
	
	if (arr1[i - 1] > arr2[j - 1]):
		# Now we need to find only k-j th element since we have found out the lowest j
		return kth(arr1, m, arr2[j:], n - j, k - j)
	else:
		# Now we need to find only k-i th element since we have found out the lowest i
		return kth(arr1[i:], m - i, arr2, n, k - i)

# Driver code
arr1 = [ 2, 3, 6, 7, 9 ]
arr2 = [ 1, 4, 8, 10 ]
m = len(arr1)
n = len(arr2)
k = 5

ans = kth(arr1, m, arr2, n, k)

if (ans == -1):
	print("Invalid query")
else:
	print(ans)
