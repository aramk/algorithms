def quicksort_r(lst):
	if len(lst) == 0:
		return []
	elif len(lst) == 1:
		return lst
	else:
		(lst, pivot) = partition(lst)
		left = quicksort_r(lst[:pivot])
		right = quicksort_r(lst[pivot+1:])
	return left + [lst[pivot]] + right

def partition(lst):
	pivot = lst[-1]
	swapIndex = 0
	for index in xrange(len(lst)-1):
		currVal = lst[index]
		if (currVal < pivot):
			oldSwap = lst[swapIndex]
			lst[swapIndex] = currVal
			lst[index] = oldSwap
			swapIndex += 1
	oldSwap = lst[swapIndex]
	lst[swapIndex] = pivot
	lst[-1] = oldSwap
	return (lst, swapIndex)

print quicksort_r([3,2,5,1,4,3])

# print partition([3,2,5,1,4,3])
