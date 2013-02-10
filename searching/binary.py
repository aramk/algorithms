def binary_search(item, lst):
	return _binary_search(item, lst, 0, len(lst))

def _binary_search(item, lst, low, high):
	# high - 1 is always the last accessible index in the range
	mid = (low + high) / 2
	if low >= high:
		return None;
	if item == lst[mid]:
		return mid;
	elif item < lst[mid]:
		return _binary_search(item, lst, low, mid)
	else:
		return _binary_search(item, lst, mid + 1, high)

print binary_search(4, [1,2,3,4])
# If we didn't have the mid + 1 in the else branch, this would cause a stack overflow
print binary_search(5, [1,2,3,4])
print binary_search(1, [1,2,3,4])
print binary_search(2, [1,2,3])
print binary_search(1, [])
