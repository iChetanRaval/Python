
def largest(arr, n):


	arr.sort()

	return arr[n-1]

arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)
