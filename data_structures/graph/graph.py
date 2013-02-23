class Node:
    def __init__(self, val = None, pre = None, post = None, directed = False, visited = False):
        self.val = val
        self.pre = pre
        self.post = post
        self.nodes = []
        self.directed = directed
        self.visited = visited

    def __repr__(self):
    	# return "[%s: %s, %s] -> %s" % (str(self.val), str(self.pre), str(self.post), str(self.nodes))
        return self.val + ' -> ' + str(self.nodes)

    def add_node(self, node):
        self.nodes.append(node)

    def remove_node(self, node):
        self.nodes.remove(node)

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
        for node in self.nodes:
            if not node.visited:
                self.post = node.explore(self.pre) + 1
        return self.post

def dfs(graph, init_callback = None):
    if init_callback is not None:
        init_callback(graph)
    for node in graph:
        if not node.visited:
            node.explore()

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

a = Node("a", directed=True)
b = Node("b", directed=True)
c = Node("c", directed=True)
d = Node("d", directed=True)
# root.add_node(a)
a.add_node(b)
b.add_node(c)
b.add_node(d)

# dfs
# print a
# dfs([a])
# print a

# c = {a: list(a.nodes)}
# for i in a.nodes:
#     print i.val
    

# print reverse([a])
