def longsub(lst):
	'''
	Longest increasing subsequence
	'''
	c = []
	for i in xrange(len(lst)):
		c.append(0)
	for i in xrange(1,len(lst)):
		c[i] = c[i-1] + 1 if lst[i] > lst[i-1] else c[i]
	return c

# lst = [2,4,3,5,6,7,4,5,6]
lst = [1,-3, 5,-2, 9,-8,-6, 4]
print longsub(lst)
