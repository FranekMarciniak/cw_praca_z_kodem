import unittest
from app import interesting_function, flatten_function

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(interesting_function(2, 3), 5)
        self.assertEqual(interesting_function(-1, 1), 0)
        self.assertEqual(interesting_function(0, 0), 0)
    def test_flatten(self):
        self.assertEqual(flatten_function([1, 2, 3]), [1, 2, 3])
        self.assertEqual(flatten_function([[1, 2], [3, 4]]), [1, 3, 2, 4])

if __name__ == '__main__':
    unittest.main()
