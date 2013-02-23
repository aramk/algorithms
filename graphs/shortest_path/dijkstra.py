from pqueue import *

INFINITY = float('inf')
REMOVED = '<removed>'

def dijkstra(G, start, end):
	
	pq = PriorityQueue()
	dist = {}
	# Add nodes into heap
	for node in G:
		d = 0 if node is start else INFINITY
		pq.push(node, d)
		dist[node] = d

	print pq

	while pq.size() > 1:
		u = pq.pop()
		print 'u: %s dist: %s' % (u, dist[u])
		for v in G[u]:
			cost_u_v = G[u][v]
			# print 'cost_u_v: ' + str(cost_u_v)
			v_dist = dist[u] + cost_u_v
			if v_dist < dist[v]:
				print ' %s->%s : v_dist %s < v_dist[v] %s ' % (u, v, str(v_dist), str(dist[v]))
				dist[v] = v_dist
				pq.push(v, v_dist)
	return dist

G = {
's':{'u':10, 'x':5},
'u':{'v':1, 'x':2},
'v':{'y':4},
'x':{'u':3, 'v':9, 'y':2},
'y':{'s':7, 'v':6}
}

print dijkstra(G, 's', 'x')
