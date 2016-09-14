import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from funcprog import core

class FuncProgCoreTestCase(unittest.TestCase):
    def test_prefix_none(self):
        self.assertEqual([1], core.prefix(1, None))

    def test_prefix_empty(self):
        self.assertEqual([1], core.prefix(1, []))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
