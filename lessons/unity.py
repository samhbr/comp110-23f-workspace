import unittest

class ZipFunctionalityTests(unittest.TestCase):
    def test_zip_empty_lists(self):
        # Test zip with empty lists
        result = list(zip([], []))
        self.assertEqual(result, [])

    def test_zip_equal_length_lists(self):
        # Test zip with lists of equal length
        result = list(zip([1, 2, 3], ['a', 'b', 'c']))
        self.assertEqual(result, [(1, 'a'), (2, 'b'), (3, 'c')])

    # Add more test methods for other scenarios

if __name__ == '__main__':
    unittest.main()
