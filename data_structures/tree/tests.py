import unittest
from bst_v import *

class TreeTest(unittest.TestCase):
	def runTest(self):
		a = BST(1)
		a.insert(2)
		a.insert(2)
		a.insert(3)
		a.insert(0)
		self.assertEqual(str(a), "[[None, 0, None], 1, [None, 2, [None, 3, None]]]")

if __name__ == '__main__':
    unittest.main()
