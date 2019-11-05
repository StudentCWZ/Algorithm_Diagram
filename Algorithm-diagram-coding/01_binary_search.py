def binary_search(list, item):
	'''low和high用于跟踪要在其中查找的列表部分'''
	low = 0
	high =len(list) - 1
	while low <= high:
		'''只要范围没有缩小到只包含一个元素，进入循环'''
		mid = (low + high) //2 # 检查中间的元素
		guess = list[mid]
		if guess == item:
			'''检查是否找到元素'''
			return mid
		elif guess < item:
			low = mid + 1
		else:
			high = mid - 1
	return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))