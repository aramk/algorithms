class Node:
    def __init__(self, name, pre = None, post = None, visited = False):
        self.name = name
        self.pre = pre
        self.post = post
        self.visited = visited

    def __repr__(self):
        return '(%s,%s,%s)' % (self.name, str(self.pre), str(self.post))

class Edge:
    def __init__(self, u = None, v = None, cost = None, pre = None, post = None, directed = False, visited = False, next = None):
        self.u = u
        self.v = v
        self.directed = directed
        self.visited = visited
        self.cost = cost

    def __repr__(self):
        return "%s %s %s" % (self.u, '->' if self.directed else '--', self.v)

    def explore(self, pre = -1):
        self.u.pre = pre + 1
        self.u.post = self.u.pre + 1
        if self.v:
            if not self.v.visited:
                self.v.pre = self.u.pre + 1
                self.v.post = self.u.post + 1
                self.u.post = self.v.post + 1

def dfs(graph, init_callback = None):
    if init_callback is not None:
        init_callback(graph)
    for e in graph:
        if not e.visited:
            e.explore()
    return graph

a = Node('a')
b = Node('b')
c = Node('c')

x = Edge(a, b, 2)
y = Edge(a, c, 3)

G = [x,y]

print G

print dfs(G)
