import os, sys, unittest

from euler21.AmicableNumbers import findAmicablePairs
from euler22.NamesScores import sumNamesScores
from euler23.NonAbundantSums import findNonAbundantSum
from euler24.LexicographicPermutations import findPermutations
from . import toInteger

class TestEuler(unittest.TestCase):

    def test21(self) :
        self.assertEqual(findAmicablePairs(10000), 31626)
    
    def test22(self) :
        path = 'euler22/names.txt'
        self.assertTrue(os.path.exists(path), \
            'Missing test file %s.' % path)
        self.assertEqual(sumNamesScores(path), 871198282)

    def test23(self) :
        self.assertEqual(findNonAbundantSum(28123), 4179871)

    def test24(self) :
        self.assertEqual(findPermutations("!"), "?")