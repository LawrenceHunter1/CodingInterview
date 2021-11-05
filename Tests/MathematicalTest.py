import unittest, random

import sys
sys.path.append("../")
from Mathematical.Fibonacci_recursive import fibonacci as fibonacciR
from Mathematical.Fibonacci_itterative import fibonacci as fibonacciI
from Mathematical.UglyNumbers import getNUglyNo
from Mathematical.BinomialCoefficient import binomialCoefficient
from Mathematical.PermutationCoefficient import permutationCoefficient

class TestRecursiveFibonacci(unittest.TestCase):
    def testZero(self):
        self.assertEqual(fibonacciR(0), 0)

    def testOne(self):
        self.assertEqual(fibonacciR(1), 1)
    
    def testToTwenty(self):
        values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 
                    377, 610, 987, 1597, 2584, 4181, 6765]
        results = []
        for i in range(0, 21):
            results.append(fibonacciR(i))
        self.assertEqual(values, results)

class TestItterativeFibonacci(unittest.TestCase):
    def testZero(self):
        self.assertEqual(fibonacciI(0), [])

    def testOne(self):
        self.assertEqual(fibonacciI(1), [1])
    
    def testToTwenty(self):
        values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 
                    377, 610, 987, 1597, 2584, 4181, 6765]
        results = []
        for i in range(0, 21):
            results.append(fibonacciR(i))
        self.assertEqual(values, results)


class TestUglyNumbers(unittest.TestCase):
    def testZero(self):
        self.assertEqual(getNUglyNo(0), [])

    def testOne(self):
        self.assertEqual(getNUglyNo(1), [1])
    
    def testToEleven(self):
        values = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15]
        self.assertEqual(getNUglyNo(11), values)

class TestBinomialCoefficient(unittest.TestCase):
    def testZero(self):
        self.assertEqual(binomialCoefficient(0, 0), 1)

    def testKOne(self):
        self.assertEqual(binomialCoefficient(0, 1), 0)

    def testNOne(self):
        self.assertEqual(binomialCoefficient(1, 0), 1)

    def testOne(self):
        self.assertEqual(binomialCoefficient(1, 1), 1)

    def testTwoOne(self):
        self.assertEqual(binomialCoefficient(2, 1), 2)

    def testTenFive(self):
        self.assertEqual(binomialCoefficient(10, 5), 252)


class TestPermutationCoefficient(unittest.TestCase):
    def testZero(self):
        self.assertEqual(permutationCoefficient(0, 0), 1)

    def testKOne(self):
        self.assertEqual(permutationCoefficient(0, 1), 0)

    def testNOne(self):
        self.assertEqual(permutationCoefficient(1, 0), 1)

    def testOne(self):
        self.assertEqual(permutationCoefficient(1, 1), 1)

    def testTwoOne(self):
        self.assertEqual(permutationCoefficient(2, 1), 2)

    def testTenFive(self):
        self.assertEqual(permutationCoefficient(10, 5), 30240)

def testSuite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRecursiveFibonacci))
    test_suite.addTest(unittest.makeSuite(TestItterativeFibonacci))
    test_suite.addTest(unittest.makeSuite(TestUglyNumbers))
    test_suite.addTest(unittest.makeSuite(TestBinomialCoefficient))
    test_suite.addTest(unittest.makeSuite(TestPermutationCoefficient))
    return test_suite

if __name__ == '__main__':
    suite = testSuite()
    runner = unittest.TextTestRunner()
    runner.run(suite)