def binary_search_r(item, lst):
	'''Recursive binary search.'''
	return _binary_search_r(item, lst, 0, len(lst))

def _binary_search_r(item, lst, low, high):
	# high - 1 is always the last accessible index in the range
	# We are searching in the range [low, high)
	mid = (low + high) / 2
	if low >= high:
		return None
	elif item == lst[mid]:
		return mid;
	elif item < lst[mid]:
		return _binary_search_r(item, lst, low, mid)
	else:
		return _binary_search_r(item, lst, mid + 1, high)

print binary_search_r(4, [1,2,3,4])
# If we didn't have the mid + 1 in the else branch, this would cause a stack overflow
print binary_search_r(5, [1,2,3,4])
print binary_search_r(1, [1,2,3,4])
print binary_search_r(2, [1,2,3])
print binary_search_r(1, [])

def binary_search_i(item, lst):
	return _binary_search_i(item, lst, 0, len(lst))

def _binary_search_i(item, lst, low, high):
	'''Iterative binary search.'''
	while low < high:
		mid = (low + high) / 2
		if lst[mid] == item:
			return mid
		elif lst[mid] < item:
			low = mid + 1
		else:
			high = mid
	return None

print binary_search_i(4, [1,2,3,4])
print binary_search_i(5, [1,2,3,4])
print binary_search_i(1, [1,2,3,4])
print binary_search_i(2, [1,2,3])
print binary_search_i(1, [])
