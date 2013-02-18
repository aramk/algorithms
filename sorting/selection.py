def selection_sort(lst):
	if len(lst) > 1:
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
