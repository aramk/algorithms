def max_sub(A):
	'''Brute force version of finding maximum sub-array.'''
	if len(A) < 2:
		return None
	else:
		maxi, maxj = 0, 1
		maxdiff = -float('inf')
		for i in xrange(len(A) - 1):
			for j in xrange(i + 1, len(A)):
				curdiff = A[j] - A[i]
				if curdiff > maxdiff:
					maxi, maxj, maxdiff = i, j, curdiff
		return (maxi, maxj, maxdiff)

def max_sub_cross(A, low, mid, high):
	'''Returns the tuple for the maximum sub-array crossing over the mid point of the delta array. Returns tuple as (i, j, sum).'''
	if low >= high:
		return (low, high, A[low])
	else:
		rightSum = leftSum = -float('inf')
		maxLeft = maxRight = mid
		currSum = 0
		for i in xrange(mid - 1, low - 1, -1):
			currSum += A[i]
			if currSum > leftSum:
				leftSum = currSum
				maxLeft = i
		currSum = 0
		for i in xrange(mid, high):
			currSum += A[i]
			if currSum > rightSum:
				rightSum = currSum
				maxRight = i
		return (maxLeft, maxRight, leftSum + rightSum)

def delta_list(A):
	'''Returns the first difference/change of the list.''' 
	delta = []
	for i in xrange(len(A)-1):
		delta.append(A[i+1] - A[i])
	return delta

def max_sub_r(A):
	'''Recursive, binary search version of finding maximum sub-array. Returns tuple as (i, j, sum).'''
	D = delta_list(A)
	return _max_sub_r(D, 0, len(D))

def _max_sub_r(A, low, high):
	# Expends A to be a delta array.
	if low >= high - 1:
		return (low, high, A[low])
	else:
		mid = (low + high) / 2
		left = (leftLow, leftHigh, leftSum) = _max_sub_r(A, low, mid)
		right = (rightLow, rightHigh, rightSum) = _max_sub_r(A, mid, high)
		cross = (crossLow, crossHigh, crossSum) = max_sub_cross(A, low, mid, high)
		if leftSum > rightSum and leftSum > crossSum:
			return left
		elif rightSum > leftSum and rightSum > crossSum:
			return right
		else:
			return cross
