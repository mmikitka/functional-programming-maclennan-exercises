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

    def test_add(self):
        self.assertEqual(10, sequence.add([0, 1, 2, 3, 4]))

    def test_prod_zero(self):
        self.assertEqual(0, sequence.prod([0, 1, 2, 3, 4]))

    def test_prod(self):
        self.assertEqual(24, sequence.prod([1, 2, 3, 4]))

    def test_append_empty(self):
        self.assertEqual([], sequence.append([]))

    def test_append(self):
        self.assertEqual(['1', '2', 'a', 'b', 'c', '@', '#'], sequence.append([['1', '2'], ['a', 'b', 'c'], ['@', '#']]))

    def test_seqand_empty(self):
        self.assertEqual(True, sequence.seqand([]))

    def test_seqand_false(self):
        self.assertEqual(False, sequence.seqand([['a', 'b'], ['1', '2'], []]))

    def test_seqand_true(self):
        self.assertEqual(True, sequence.seqand([['a', 'b'], ['1', '2'], ['@', '#']]))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
