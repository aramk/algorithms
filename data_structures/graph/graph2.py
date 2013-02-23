class Edge:
    def __init__(self, name = None, cost = None, pre = None, post = None, directed = False, visited = False, next = None):
        self.name = name
        self.pre = pre
        self.post = post
        self.nodes = []
        self.directed = directed
        self.visited = visited
        self.cost = cost
        self.next = next

    def __repr__(self):
    	# return "[%s: %s, %s] -> %s" % (str(self.val), str(self.pre), str(self.post), str(self.nodes))
        return self.name + '(%s,%s) --(%s)>> %s' % (str(self.pre), str(self.post), str(self.cost), str(self.next))

    # def dfs(self, init_callback = None):
    #     if init_callback is not None:
    #         init_callback(self)
    #     if not self.visited:
    #         self.explore(self.pre)
    #     for node in self.nodes:
    #         if not node.visited:
    #             node.explore(self.pre)
    #         print node

    def explore(self, pre = -1):
        self.pre = pre + 1
        self.post = self.pre + 1
        if self.next:
            if not self.next.visited:
                self.post = self.next.explore(self.pre) + 1
        return self.post

def dfs(graph, init_callback = None):
    if init_callback is not None:
        init_callback(graph)
    for e in graph:
        if not e.visited:
            e.explore()
    return graph

# def reverse(graph):
#     rev = {}
#     for parent in graph:
#         for child in parent.nodes:
#             if child in rev:
#                 rev[child].append(parent)
#             else:
#                 rev[child] = [parent]
#         parent.nodes = []
#     print rev

# a = Node("a", directed=True)
# b = Node("b", directed=True)
# c = Node("c", directed=True)
# d = Node("d", directed=True)
# root.add_node(a)
# a.add_node(b)
# b.add_node(c)
# b.add_node(d)

# dfs
# print a
# dfs([a])

a = Edge("w")
b1 = Edge("x")
b2 = Edge("x")
c = Edge("y")
d = Edge("z")

a.next = b
a.cost = 3
b.next = c
b.cost = 4
c.next = d
c.cost = 5

G = [a]

print G

print dfs(G)

# c = {a: list(a.nodes)}
# for i in a.nodes:
#     print i.val
    

# print reverse([a])
