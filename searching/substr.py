def substr(query, target): for i in xrange(len(target)): for j in
	xrange(len(query)): found = True if (query[j] != target[i+j]): found =
	False break; if found: return i return False

print substr("bob", "spongebob")
