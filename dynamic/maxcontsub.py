def maxcontsub(A):
	'''Maximum Value Contiguous Subsequence.'''
	M=[None for x in A]
	for i in range(len(A)):
		if i == 0:
			M[i] = A[i]
		else:
			M[i] = max( M[i-1] + A[i] , A[i] )
	return M

print maxcontsub([1, -3, 5, -2, 9, -8, -6, 4])
