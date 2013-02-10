def lcs2(l1, l2):
	L = [[0 for x in range(len(l2))] for y in range(len(l1))]
	pre = []
	maxi = 0
	for i in xrange(len(l1)):
		for j in xrange(len(l2)):
			if l1[i] == l2[j] and i != 0 and j != 0:
				L[i][j] = L[i-1][j-1] + 1
			else:
				max( L[i][j-1] , L[i-1][j] )
	print L

def last(pre, maxi, a):
	follow = pre[maxi]
	if follow < 0:
		return a
	else:
		a = [follow] + a
		return last(pre, follow, a)

lcs2([0,2,8,4], [1,2,8,4,1])
