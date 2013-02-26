import unittest
from max_subarray import *
from matrix import *

class MaxSubArrayTest(unittest.TestCase):
	def runTest(self):
		A = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
		# This works with the original A list
		self.assertEqual(max_sub(A), (7, 11, 43));
		# These work on the first difference
		self.assertEqual(max_sub_r(A), (7, 11, 43));
		self.assertEqual(max_sub_linear(delta_list(A)), (7, 11, 43));

class MatrixTest(unittest.TestCase):
	def runTest(self):
		self.assertEqual(matrix_mult([[1,2],[3,4]], [[5,6],[7,8]]), [[19, 22], [43, 50]]);
		self.assertEqual(matrix_mult([[1,2, 3,4]], [[5],[6],[7],[8]]), [[70]]);

if __name__ == '__main__':
    unittest.main()
