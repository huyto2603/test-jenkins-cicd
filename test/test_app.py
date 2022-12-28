import unittest
from app import fibonacci, factorial


class TestFibonacii(unittest.TestCase):
    def test_fibonacii_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacii_10(self):
        self.assertEqual(fibonacci(10), 89)

    def test_fibonacii_30(self):
        self.assertEqual(fibonacci(30), 1346269)


class TestFactorial(unittest.TestCase):
    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)
