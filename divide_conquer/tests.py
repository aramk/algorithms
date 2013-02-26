import unittest
from max_subarray import *

class MaxSubArrayTest(unittest.TestCase):
	def runTest(self):
		A = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
		# This works with the original A list
		self.assertEqual(max_sub(A), (7, 11, 43));
		# These work on the first difference
		self.assertEqual(max_sub_r(A), (7, 11, 43));
		self.assertEqual(max_sub_linear(delta_list(A)), (7, 11, 43));

if __name__ == '__main__':
    unittest.main()
