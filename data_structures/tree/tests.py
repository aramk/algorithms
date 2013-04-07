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
		a = BST(7)
		a.insert(5)
		a.insert(10)
		a.insert(4)
		a.insert(6)
		a.insert(9)
		a.insert(12)
		a.delete(7)
		predecessor = '[[[None, 4, None], 5, None], 6, [[None, 9, None], 10, [None, 12, None]]]'
		successor = '[[[None, 4, None], 5, [None, 6, None]], 9, [None, 10, [None, 12, None]]]'
		self.assertTrue(str(a) == predecessor or str(a) == successor)


if __name__ == '__main__':
    unittest.main()
