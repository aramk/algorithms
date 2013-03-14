def quicksort_r(lst):
	if len(lst) == 0:
		return []
	elif len(lst) == 1:
		return lst
	else:
		(lst, pivot) = partition(lst, 0, len(lst))
		left = quicksort_r(lst[:pivot])
		right = quicksort_r(lst[pivot+1:])
	return left + [lst[pivot]] + right

def partition(A, p, r):
	pivotIndex = r-1
	swapIndex = 0
	for i in xrange(r-1):
		if A[i] < A[pivotIndex]:
			swap(A, swapIndex, i)
			swapIndex += 1
	swap(A, swapIndex, pivotIndex)
	return (A, swapIndex)

def swap(A, i, j):
	tmp = A[i]
	A[i] = A[j]
	A[j] = tmp
