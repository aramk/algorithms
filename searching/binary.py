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

def binary_sum(sum, lst):
	'''Finds whether the given sum exists from the addition of two items in the sorted list'''
	for i in xrange(0, len(lst)):
		rem = sum - lst[i]
		j = binary_search_i(rem, lst)
		if j:
			return (i, j)
	return None
