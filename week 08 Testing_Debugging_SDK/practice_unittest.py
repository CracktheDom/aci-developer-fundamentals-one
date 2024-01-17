import unittest


def add(x, y):
    return x + y


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 5), 10)

    def test_add_two_negative(self):
        self.assertEqual(add(-3, -7) - 10)


if __name__ == "__main__":
    unittest.main()
