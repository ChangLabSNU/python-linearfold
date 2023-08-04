from unittest import TestCase
from array import array
from linearfold import fold

class TestLinearFold(TestCase):

    seq1 = 'UGUCGGGUAGCUUAUCAGACUGAUGUUGACUGUUGAAUCUCAUGGCAACACCAGUCGAUGGGCUGUCUGACA'
    fold1 = '((((((((((((((((.(((((.(((((.(((.(((...))))))))))).)))))))))))))))))))))'
    mfe1 = -34.6

    def test_1(self):
        self.assertEqual(fold(self.seq1), (self.fold1, self.mfe1))

if __name__ == '__main__':
    import unittest
    unittest.main()
