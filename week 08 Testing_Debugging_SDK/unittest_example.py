# https://docs.python.org/3/library/unittest.html#organizing-tests

import unittest


class ExampleTestCase(unittest.TestCase):
    def setUp(self):
        self.x = 100
        self.y = 50

    def tearDown(self):
        self.x = None
        self.y = None

    def test_addition(self):
        result = self.x + self.y
        self.assertEqual(result, 150)

    def test_subtraction(self):
        result = self.x - self.y
        self.assertEqual(result, 50)


if __name__ == "__main__":
    unittest.main()
