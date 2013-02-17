def merge(a, b):
	'''
	Merges two sorted lists.
	'''
	indexA = 0
	indexB = 0
	c = []
	while indexA < len(a) and indexB < len(b):
		currA = a[indexA]
		currB = b[indexB]
		if currA < currB:
			c.append(currA)
			indexA += 1
		else:
			c.append(currB)
			indexB += 1
	if indexA < len(a):
		c += a[indexA:]
	elif indexB < len(b):
		c += b[indexB:]
	return c

def merge2(A, p, q, r):
	'''
	Merges two sorted lists which exist in a single list.
	A[p:q] is the first sorted list, A[q:r] is the second.
	Uses a sentinel for each sublist. Merges in situ.
	'''
	n1 = q-p
	n2 = r-q
	i = j = 0
	infinity = float('inf')
	sentinel = [infinity]
	L = A[p:q] + sentinel
	R = A[q:r] + sentinel
	for k in xrange(p, r):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1

def half_list(a):
	return a[:len(a)/2]

def split_list(a):
	return (a[:len(a)/2], a[len(a)/2:])

def mergesort_r(a):
	if len(a) == 0:
		return []
	elif len(a) == 1:
		return a;
	else:
		(left, right) = split_list(a)
		left = mergesort_r(left)
		right = mergesort_r(right)
		return merge(left, right)

def mergesort_r2(A, p, r):
	if p >= r - 1:
		return
	else:
		mid = (p + r) / 2
		mergesort_r2(A, p, mid)
		mergesort_r2(A, mid, r)
		merge2(A, p, mid, r)
		return A

print mergesort_r2([2,3,1,4,6], 0, 5)
