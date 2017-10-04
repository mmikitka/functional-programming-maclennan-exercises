import unittest
import os
import sys
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from funcprog import higherorder

class FuncProgHigherOrderTestCase(unittest.TestCase):
    def test_mapf_sqrt(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], higherorder.mapf(math.sqrt, [1, 4, 9, 16, 25, 36]))

    def test_mapf_matrix_square(self):
        """ Exercise 6.18.a """
        self.assertEqual([[1, 4], [9, 16]], higherorder.mapf(higherorder.mapf(self.square, [[1, 2], [3, 4]])))

    def square(self, v):
        return pow(v, 2)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
