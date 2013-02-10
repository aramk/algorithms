def linear_search(item, lst):
	for i in lst:
		if lst[i] == item:
			return i
	return None

print linear_search(4, [3,2,4,1])
