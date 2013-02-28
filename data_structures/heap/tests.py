import unittest
from heap import *

class HeapTest(unittest.TestCase):
	def runTest(self):
		self.assertEqual(Heap([1,4,3,2,5]).heapify(0), [4,5,3,2,1])
		self.assertEqual(Heap([27,17,3,16,13,10,1,5,7,12,4,8,9,0]).heapify(2), [27,17,10,16,13,9,1,5,7,12,4,8,3,0])

if __name__ == '__main__':
    unittest.main()
