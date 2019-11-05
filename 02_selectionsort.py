def findSmallest(arr):
	smallest = arr[0] # 存储最小的值
	smallest_index = 0 # 存储最小元素的索引
	for i in range(len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
		else:
			pass
	return smallest_index


def selectionSort(arr):
	'''对数组进行排序'''
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr) # 找出数组中最小的元素，并将其加入到新的数组中。
		newArr.append(arr.pop(smallest))
	return newArr


print(selectionSort([5, 3, 6, 2, 10]))