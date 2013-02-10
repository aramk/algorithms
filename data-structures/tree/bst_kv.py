class BST:
    def __init__(self, key, val=None):
        self.left = None
        self.right = None
        self.key = key
        self.val = val

    def __str__(self):
    	return "[%s, %s:%s, %s]" % (self.left, str(self.key), str(self.val), self.right)

    def isEmpty(self):
    	return self.left == self.right == self.val == None

    def insert(self, key, val):
    	if self.isEmpty():
    		self.key = key
    		self.val = val
        elif self.key == key:
            self.val = val
    	elif key < self.key:
    		if self.left is None:
    			self.left = BST(key, val)
    		else:
    			self.left.insert(key, val)
    	else:
    		if self.right is None:
    			self.right = BST(key, val)
    		else:
    			self.right.insert(key, val)
    
    def find(self, key):
        if self.isEmpty():
            return None
        elif self.key == key:
            return self.val
        elif key < self.key:
            return self.left.find(key) if self.left else None
        else:
            return self.right.find(key) if self.right else None

    def delete(self, key):
        pass

# Insert
a = BST(2, "two")
a.insert(1, "one")
a.insert(3, "three")
# print a
a.insert(2, "newtwo")
# print a

# Find
print a.find(3)
