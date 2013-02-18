def bubble_sort(lst):
	if len(lst) > 1:
		for i in xrange(len(lst) - 1):
			changed = False
			for j in xrange(i, len(lst)):
				if lst[j] < lst[i]:
					tmp = lst[j]
					lst[j] = lst[i]
					lst[i] = tmp
					changed = True
			if not changed:
				break
	return lst
