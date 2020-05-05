import sys, unittest

from euler21.AmicableNumbers import findAmicablePairs
from Util.General import toInteger

class TestStringMethods(unittest.TestCase):

    def testAll(self):
        self.assertEqual(findAmicablePairs(toInteger(sys.argv[1])), 'FOO')

if __name__ == '__main__':
    unittest.main()