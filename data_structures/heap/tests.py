import unittest
from heap import *
from priority_queue import *

class HeapTest(unittest.TestCase):
	def runTest(self):
		self.assertEqual(Heap([1,4,3,2,5]).heapify(0), [5,4,3,2,1])
		self.assertEqual(Heap([27,17,3,16,13,10,1,5,7,12,4,8,9,0]).heapify(2), [27,17,10,16,13,9,1,5,7,12,4,8,3,0])
		self.assertEqual(Heap([4,1,5,1,5,8]).build(), [8,5,5,1,1,4])
		self.assertEqual(Heap([8,4,1,5,2,3,7]).sort(), [1,2,3,4,5,7,8])

class PriotityQueueTest(unittest.TestCase):
	def runTest(self):
		pq = PriorityQueue([4,1,5,3])
		self.assertEqual(pq.extractMax(), 5)
		self.assertEqual(pq.extractMax(), 4)
		self.assertEqual(pq.extractMax(), 3)
		self.assertEqual(pq.extractMax(), 1)
		self.assertRaises(Exception, pq.extractMax)

		pq = PriorityQueue([5,4,2,5,6])
		pq.increase(3, 8)
		self.assertEqual(pq, [8,6,2,5,4])

		pq = PriorityQueue([5,4,2,5,6])
		pq.insert(8)
		self.assertEqual(pq, [8,5,6,5,4,2])

if __name__ == '__main__':
    unittest.main()
