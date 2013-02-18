import unittest
from bubble import *
from selection import *

class BubbleTest(unittest.TestCase):
	def runTest(self):
		self.assertEqual(bubble_sort([3,2,4,1]), [1,2,3,4]);

class SelectionTest(unittest.TestCase):
	def runTest(self):
		self.assertEqual(selection_sort([3,2,4,1]), [1,2,3,4]);

if __name__ == '__main__':
    unittest.main()
