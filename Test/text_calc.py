import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(3, 5), 8)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 2), 3)

    def test_divide(self):
        # self.assertRaises(ValueError, calc.divide, 10, 0)
        # context manager
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    # run all of us tests.
    # each function is a test.
    unittest.main()
