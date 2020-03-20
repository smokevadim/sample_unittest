import os
import sys
import unittest

sys.path.append(os.getcwd())
from sample import *


class TestABC(unittest.TestCase):
    def test_sort_it_return_ABC(self):
        self.assertEqual(sort_it(['C', 'A', 'B']), ['A', 'B', 'C'])
        self.assertEqual(sort_it(['d', 'c', 'a']), ['a', 'c', 'd'])

    def test_sort_it_return_type(self):
        self.assertIsInstance(sort_it(('a', 'b', 'c')), list)


if __name__ == '__main__':
    unittest.main()
