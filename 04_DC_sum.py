
def sum(arr):
	b = 0
	for i in arr:
		b += 1
	if b == 1:
		return arr[0]
	else:
		x = arr[0]
		arr.pop(0)
		sum_arr = x + sum(arr)
		return sum_arr

print(sum([5,2,3,4]))
