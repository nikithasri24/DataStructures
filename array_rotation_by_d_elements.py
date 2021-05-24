import array

def rotate(arr, d, n):
	temp = 0
	for i in range(0,d):
		temp = arr[0]
		for j in range(0,n-1):
			arr[j] = arr[j+1]
		arr[n-1] = temp
	print(arr)

arr = [1,2,3,4,5,6]

rotate(arr,2,6)
