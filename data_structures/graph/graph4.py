from collections import deque

class Node:
    def __init__(self, name, visited = False):
        self.name = name
        self.visited = visited
        self.edges = set()

    def __repr__(self):
        return '(%s,%s,%s)' % (self.name, str(self.pre), str(self.post))

    def dfs(self, pre=0, order={}):
        self.visited = True
        post = pre
        for e in self.edges:
            if not e.v.visited:
                e.v.dfs(pre=post + 1, order=order)
                post = order[e.v.name][1]
        order[self.name] = (pre, post + 1)
        return order

    def bfs(self):
        to_visit = deque()
        to_visit.append(self)
        dist = {self.name: 0}
        while len(to_visit) > 0:
            u = to_visit.popleft()
            u.visited = True
            for e in u.edges:
                if not e.v.visited:
                    to_visit.append(e.v)
                    dist[e.v.name] = dist[u.name] + 1
        return dist

class Edge:
    def __init__(self, u, v, cost = None, pre = None, post = None, directed = False, visited = False, next = None):
        self.u = u
        self.v = v
        self.directed = directed
        self.visited = visited
        self.cost = cost
        self.u.edges.add(self)
        if not directed:
            self.v.edges.add(self)

    def __repr__(self):
        return "%s %s %s" % (self.u, '->' if self.directed else '--', self.v)

# TODO inelegant
def reset(G):
    for u in G:
        u.visited = False

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

x = Edge(a, b, 2)
y = Edge(a, c, 3)
z = Edge(b, d, 3)

# TODO inelegant
G = set([a,b,c,d])

print a.dfs()
reset(G)
print a.bfs()
