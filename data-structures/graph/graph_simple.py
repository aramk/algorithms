a = {
	'a' : ['b', 'c'],
	'b' : ['d', 'e'],
	'c' : ['d']
}

def reverse(graph):
	rev = {}
	for parent in graph:
		children = graph[parent]
		for child in children:
			if child in rev:
				rev[child].append(parent)
			else:	
				rev[child] = [parent]
	return rev

print reverse(a)
