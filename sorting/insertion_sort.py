def insertion_sort(lst, increasing=True):
	for i in xrange(1,len(lst)):
		key = lst[i]
		j = i - 1;
		while j >= 0 and (lst[j] > key if increasing else lst[j] < key):
			lst[j + 1] = lst[j]
			j -= 1
		lst[j + 1] = key
	return lst

print insertion_sort([3,2,5,1,4,3])

print insertion_sort([3,2,5,1,4,3], increasing=False)