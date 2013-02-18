def linear_search(item, lst):
	for i in lst:
		if lst[i] == item:
			return i
	return None
