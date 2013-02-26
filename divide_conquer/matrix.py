def matrix_mult(A, B):
	'''Brute-force matrix multiplication.'''
	C = []
	n = len(B)
	rows = len(A)
	cols = len(B[0])
	for i in xrange(rows):
		C.append([0] * cols)
		for j in xrange(cols):
			for k in xrange(n):
				C[i][j] += A[i][k] * B[k][j]
	return C

