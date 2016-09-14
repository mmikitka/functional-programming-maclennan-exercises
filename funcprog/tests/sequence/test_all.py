import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from funcprog import sequence

class FuncProgSequenceTestCase(unittest.TestCase):
    def test_elt_first(self):
        self.assertEqual('a', sequence.elt(['a', 'b', 'c'], 0))

    def test_elt_last(self):
        self.assertEqual('c', sequence.elt(['a', 'b', 'c'], 2))

    def test_cat(self):
        self.assertEqual(['a', 'b', 'c', '1', '2', '3'], sequence.cat(['a', 'b', 'c'], ['1', '2', '3']))

    def test_indsubst_within(self):
        self.assertEqual(['a', 'b', 'c'], sequence.indsubst('b', 1, ['a', 'z', 'c']))

    def test_indsubst_beyond(self):
        self.assertEqual(['a', 'b', 'c'], sequence.indsubst('c', 4, ['a', 'b']))

    def test_subst1st(self):
        self.assertEqual(['a', '2', 'c'], sequence.subst1st('2', 'b', ['a', 'b', 'c']))

    def test_subst_multiple(self):
        self.assertEqual(['the', 'cat', 'likes', 'cat', 'food'], sequence.subst('cat', 'animal', ['the', 'animal', 'likes', 'animal', 'food']))

    def test_subst_nomatch(self):
        self.assertEqual(['the', 'animal', 'likes', 'animal', 'food'], sequence.subst('cat', 'tree', ['the', 'animal', 'likes', 'animal', 'food']))

    def test_lsubst(self):
        self.assertEqual(['c', 'o', 'u', 'n', 't', '=', 'c', 'o', 'u', 'n', 't', '+', '1'], sequence.lsubst(['c', 'o', 'u', 'n', 't'], 'x', ['x', '=', 'x', '+', '1']))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
