import random, time, copy

default_cmp = lambda x,y: x < y

def quicksort_r(A, cmp = default_cmp, rand = False):
	if len(A) == 0:
		return []
	elif len(A) == 1:
		return A
	else:
		if rand:
			pivotIndex = len(A) - 1
			randIndex = random.randint(0, pivotIndex)
			swap(A, randIndex, pivotIndex)
		(A, pivot) = partition(A, 0, len(A), cmp)
		left = quicksort_r(A[:pivot], cmp)
		right = quicksort_r(A[pivot+1:], cmp)
	return left + [A[pivot]] + right

def partition(A, p, r, cmp = default_cmp):
	if p == r-1:
		return (A, p)
	elif p > r-1 or len(A) == 0:
		return (A, None)
	else:
		pivotIndex = r-1
		swapIndex = p
		for i in xrange(p, r-1):
			if cmp(A[i], A[pivotIndex]):
				swap(A, swapIndex, i)
				swapIndex += 1
		swap(A, swapIndex, pivotIndex)
		return (A, swapIndex)

def find_kth(A, k):
	'''Find kth largest element in list A'''
	return _find_kth(A, k, 0, len(A))

def _find_kth(A, k, p, r):
	(A, pivotIndex) = partition(A, p, r)
	if k == pivotIndex:
		return A[k]
	elif (k < pivotIndex):
		return _find_kth(A, k, p, pivotIndex)
	else:
		return _find_kth(A, k, pivotIndex + 1, r)

def swap(A, i, j):
	tmp = A[i]
	A[i] = A[j]
	A[j] = tmp


print partition([5,4, 1, 3,2], 0, 5)
