def merge(a, b):
	'''
	Take two sorted lists, run a loop and take smallest of element of each given their
	current index until said index reaches the end of its list
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

#print merge([10,13,15], [2,14,16])

def half_list(a):
	return a[:len(a)/2]

def split_list(a):
	return (a[:len(a)/2], a[len(a)/2:])

# print split_list([2,4,2,1,4,3,4])

def mergesort_r(a):
	'''
	Take a list and recursively merge each half
	'''
	if len(a) == 0:
		return []
	elif len(a) == 1:
		return a;
	else:
		(left, right) = split_list(a)
		left = mergesort_r(left)
		right = mergesort_r(right)
		return merge(left, right)

print mergesort_r([2,3,1,4,6])

