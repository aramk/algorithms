def longsubseq(lst):
	L = [1 for x in lst] # LIS up to each x
	B = [-1 for x in lst] # The best j leading up to the x (last item)
	for i in range(len(lst)):
		for j in range(i):
			if (lst[j] < lst[i] and L[j] + 1 > L[i]):
				L[i] = L[j] + 1
				B[i] = j
	return L, B

print longsubseq([5,2,8,6,3,6,9,7])
