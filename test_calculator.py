# https://github.com/0-0Yoshi0-0/lab11-YS-HT
# Partner 1: Yash Singh
# Partner 2: Henry Tang

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(-6,-8), -14)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3,2), 1)
        self.assertEqual(subtract(-5,-10), 5)
        self.assertEqual(subtract(25,50), -25)


    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(2, 10), 5.0)
        self.assertEqual(div(4, 20), 5.0)
        self.assertAlmostEqual(div(3, 10), 3.333333333)

    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2,4), 0.5)
        self.assertAlmostEqual(logarithm(27,3), 3)
        self.assertEqual(logarithm(64,8), 2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(-1,9)


    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0, 10)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(1, 1), 1.414213562)

    def test_sqrt(self):  # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(16), 4.0)
        self.assertAlmostEqual(square_root(2), 1.414213562)
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()