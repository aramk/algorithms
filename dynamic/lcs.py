def lcs(lst):
	L = []
	pre = []
	maxi = 0
	for i in xrange(len(lst)):
		L.append(0);
		pre.append(-1);
	for i in xrange(len(lst)):
		for j in xrange(i+1, len(lst)):
			if lst[j] > lst[i]:
				L[j] = L[i] + 1
				pre[j] = i
				print (i,j), L[j]
				if L[j] > L[maxi]:
					maxi = j
		print
	print "list ", lst
	print "length ",L
	print "pre ",pre

	last_ = last(pre, maxi, [maxi])
	print "path ",last_

def last(pre, maxi, a):
	follow = pre[maxi]
	if follow < 0:
		return a
	else:
		a = [follow] + a
		return last(pre, follow, a)

lcs([1,4,3,2,5,7,8,3])
# lcs([1,2,8,4])
