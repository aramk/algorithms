def selection_sort(lst):
	if len(lst) == 0:
		return lst
	else:
		# We don't need to loop for last item (already the min)
		for i in xrange(len(lst) - 1):
			minIndex = i
			for j in xrange(i, len(lst)):
				if lst[j] < lst[minIndex]:
					minIndex = j
			swapIndex(lst, i, minIndex)
		return lst

def swapIndex(lst, source, dest):
	tmp = lst[dest]
	lst[dest] = lst[source]
	lst[source] = tmp

'''
Unlike insertion sort, these all take the same amount of runtime.
'''
print selection_sort([3,2,5,1,4])
print selection_sort([1,2,3,4,5])
print selection_sort([5,4,3,2,1])
