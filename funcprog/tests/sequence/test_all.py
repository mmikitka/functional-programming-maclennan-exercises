import unittest
import os
import sys
import math

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from funcprog import sequence

class FuncProgSequenceTestCase(unittest.TestCase):
    def test_elt_first(self):
        self.assertEqual('a', sequence.elt(['a', 'b', 'c'], 0))

    def test_elt_last(self):
        self.assertEqual('c', sequence.elt(['a', 'b', 'c'], 2))

    def test_cat(self):
        self.assertEqual(['a', 'b', 'c', '1', '2', '3'], sequence.cat(['a', 'b', 'c'], ['1', '2', '3']))

    def test_trans2(self):
        self.assertEqual([['a', '1'], ['b', '2'], ['c', '3']], sequence.trans2(['a', 'b', 'c'], ['1', '2', '3']))

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
        self.assertEqual([], sequence.seqand([]))

    def test_seqand_false(self):
        self.assertEqual([], sequence.seqand([['a', 'b'], ['1', '2'], []]))

    def test_seqand_true(self):
        self.assertEqual(['@', '#'], sequence.seqand([['a', 'b'], ['1', '2'], ['@', '#']]))

    def test_seqor_empty(self):
        self.assertEqual([], sequence.seqor([]))

    def test_seqor_false(self):
        self.assertEqual(None, sequence.seqor([[], [], [], None]))

    def test_seqor_true(self):
        self.assertEqual(['a', 'b'], sequence.seqor([['a', 'b'], [], [], None, ['@', '#']]))

    def test_seqdif(self):
        self.assertEqual(-3, sequence.seqdif([1, 10, 5, 6, 7]))

    def test_seqmin_empty(self):
        self.assertEqual(None, sequence.seqmin([]))

    def test_seqmin(self):
        self.assertEqual(1, sequence.seqmin([9, 8, 7, 6, 5, 4, 3, 2, 1]))

    def test_sublis_1(self):
        self.assertEqual(['the', 'mouse', 'in', 'the', 'house'], sequence.sublis([['X', 'mouse'], ['Y', 'house']], ['the', 'X', 'in', 'the', 'Y']))

    def test_sublis_2(self):
        self.assertEqual(['the', 'cat', 'in', 'the', 'hat'], sequence.sublis([['X', 'cat'], ['Y', 'hat']], ['the', 'X', 'in', 'the', 'Y']))

    def test_subpair(self):
        self.assertEqual(['2', '12', 'x', '+', '-2', '+', '5', '-', '12'], sequence.subpair(['a', 'b', 'c'], ['12', '-2', '5'], ['2', 'a', 'x', '+', 'b', '+', 'c', '-', 'a']))

    def test_map_sin(self):
        self.assertEqual([0.0, 1.0], sequence.map_sin([math.radians(0), math.radians(90)]))

    def test_map_prod(self):
        self.assertEqual([6, 24, 3, 1, 25], sequence.map_prod([[2, 3], [1, 4, 6], [3], [], [5, 5]]))

    def test_vector_prod(self):
        self.assertEqual([6, 8, 0], sequence.vector_prod([2, 4, 1], [3, 2, 0]))

    def test_map_dif(self):
        self.assertEqual([-1, 3, 3, 0, 0], sequence.map_dif([[2, 3], [1, 4, 6], [3], [], [5, 5]]))

    def test_seqinterval(self):
        self.assertEqual([0, 1, 2, 3], sequence.seqinterval(0, 4))

    def test_seqinterval_reverse(self):
        self.assertEqual([3, 2, 1, 0], sequence.seqinterval(4, 0))

    def test_subseq_1(self):
        self.assertEqual([0, 1, 2], sequence.subseq([0, 1, 2, 3, 4], 0, 3))

    def test_subseq_2(self):
        self.assertEqual([2, 3], sequence.subseq([0, 1, 2, 3, 4], 2, 4))

    def test_subseq_3(self):
        self.assertEqual([], sequence.subseq([0, 1, 2, 3, 4], 3, 3))

    def test_subseq_4(self):
        self.assertEqual([4, 3, 2], sequence.subseq([0, 1, 2, 3, 4], 5, 2))

    def test_subseq_5(self):
        self.assertEqual([3, 2, 1, 0], sequence.subseq([0, 1, 2, 3, 4], 4, 0))

    def test_subseq_6(self):
        self.assertEqual([], sequence.subseq([0, 1, 2, 3, 4], 3, -2))

    def test_seqcollate(self):
        self.assertEqual([2, 3, 3, 5, 6, 6, 7, 8, 9, 10, 12], sequence.seqcollate([2, 5, 6, 8, 12], [3, 3, 6, 7, 9, 10]))

    def test_seqcollateunique(self):
        self.assertEqual([2, 3, 5, 6, 7, 8, 9, 10, 12], sequence.seqcollateunique([2, 5, 6, 8, 12], [3, 3, 6, 7, 9, 10]))

    def test_seqcollatereduce(self):
        self.assertEqual([1, 2, 3, 3, 5, 6, 6, 7, 8, 9, 10, 12, 13], sequence.seqcollatereduce([[2, 5, 6, 8, 12], [3, 3, 6, 7, 9, 10], [1, 13]]))

    def test_seqdedup_asc(self):
        self.assertEqual([1, 3, 4, 5, 8, 9, 10], sequence.seqdedup([1, 1, 3, 4, 5, 8, 8, 9, 10, 10]))

    def test_seqdedup_desc(self):
        self.assertEqual([10, 9, 8, 5, 4, 3, 1], sequence.seqdedup([10, 10, 9, 8, 8, 5, 4, 3, 1, 1]))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
