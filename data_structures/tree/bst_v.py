import random
from collections import deque

class BST:

	# TODO remove the need to keep checking for None case of left and right nodes

	def __init__(self, val=None):
		self.left = None
		self.right = None
		self.val = val
		self.parent = None

	def __str__(self):
		return "[%s, %s, %s]" % (self.left, str(self.val), self.right)

	def isEmpty(self):
		return self.left == self.right == self.val is None

	def insert(self, val):
		if self.isEmpty():
			self.val = val
		elif val == self.val:
			return
		elif val < self.val:
			if self.left is None:
				self.left = BST(val)
				self.left.parent = self
			else:
				self.left.insert(val)
		else:
			if self.right is None:
				self.right = BST(val)
				self.right.parent = self
			else:
				self.right.insert(val)

	def flatten(self):
		if self.isEmpty():
			return []
		else:
			left = [] if self.left is None else self.left.flatten()
			right = [] if self.right is None else self.right.flatten()
			return left + [self.val] + right

	def replace_in_parent(self, val=None):
		if self.parent:
			if self.parent.left == self:
				self.parent.left = val
			elif self.parent.right == self:
				self.parent.right = val
			if val:
				val.parent = self.parent

	def delete(self, val):
		if val < self.val and self.left:
			self.left.delete(val)
		elif val > self.val and self.right:
			self.right.delete(val)
		else:
			if self.left and self.right:
				# TODO randomise with min and max
				rand = random.randint(0, 1)
				if rand == 0:
					# predecessor
					repl = self.left.max()
				else:
					# successor
					repl = self.right.min()
				repl.replace_in_parent(None)
				self.val = repl.val
			elif self.left:
				self.replace_in_parent(self.left)
			elif self.right:
				self.replace_in_parent(self.right)
			else:
				self.replace_in_parent(None)

	def min(self):
		curr = self
		while curr.left:
			curr = curr.left
		return curr

	def max(self):
		curr = self
		while curr.right:
			curr = curr.right
		return curr

	def dfs(self, visitor):
		visitor(self)
		if self.left:
			self.left.dfs(visitor)
		if self.right:
			self.right.dfs(visitor)

	def bfs(self, visitor):
		to_visit = deque([self])
		while len(to_visit):
			node = to_visit.popleft()
			visitor(node)
			if node.left:
				to_visit.append(node.left)
			if node.right:
				to_visit.append(node.right)

def visitor(node):
	print node.val

# a.dfs(visitor)
a.bfs(visitor)

