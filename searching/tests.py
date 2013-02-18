import unittest
from binary import *

class BinaryTest(unittest.TestCase):
	def runTest(self):
		self.assertEqual(binary_search_r(4, [1,2,3,4]), 3);
		self.assertEqual(binary_search_r(1, [1,2,3,4]), 0);
		self.assertEqual(binary_search_r(2, [1,2,3]), 1);
		self.assertEqual(binary_search_r(1, []), None);

		self.assertEqual(binary_search_i(4, [1,2,3,4]), 3);
		self.assertEqual(binary_search_i(1, [1,2,3,4]), 0);
		self.assertEqual(binary_search_i(2, [1,2,3]), 1);
		self.assertEqual(binary_search_i(1, []), None);

		self.assertEqual(binary_sum(11, [2,5,6,3,8]), (1,2));

if __name__ == '__main__':
    unittest.main()
