import unittest, random

import sys
sys.path.append("../")
from Search.BinarySearchRecursive import binarySearchHandler as binarySearchR
from Search.BinarySearchIterative import binarySearch as binarySearchI
from Search.DFS import dfsHandler as dfs
from Search.BFS import bfsHandler as bfs

def genList(size):
        return [random.randint(0, 100) for _ in range(size)]


def genListAndSorted(size):
    temp = genList(size)
    temp_sorted = temp
    temp_sorted.sort()
    return temp, temp_sorted


class TestRecursiveBinary(unittest.TestCase):
    def testEmpty(self):
        self.assertEqual(binarySearchR([], 1), False)

    def testOneTrue(self):
        self.assertEqual(binarySearchR([1], 1), True)

    def testOneFalse(self):
        self.assertEqual(binarySearchR([1], 2), False)

    def testTwoTrueOne(self):
        self.assertEqual(binarySearchR([1, 2], 1), True)

    def testTwoTrueTwo(self):
        self.assertEqual(binarySearchR([1, 2], 2), True)

    def testTwoFalse(self):
        self.assertEqual(binarySearchR([1, 2], 3), False)

    def testNegativeTrueNeg(self):
        self.assertEqual(binarySearchR([-2, -1, 0, 1, 2], -2), True)

    def testNegativeTruePos(self):
        self.assertEqual(binarySearchR([-2, -1, 0, 1, 2], 2), True)

    def testNegativeFalse(self):
        self.assertEqual(binarySearchR([-2, -1, 0, 1, 2], 3), False)
    
    def testMiddle(self):
        self.assertEqual(binarySearchR([-2, -1, 0, 1, 2], 0), True)

    def testNonIntTrue(self):
        self.assertEqual(binarySearchR([-2.5, -1.25, 10.89, 231.8], 231.8), True)

    def testNonIntFalse(self):
        self.assertEqual(binarySearchR([-2.5, -1.25, 10.89, 231.8], -11.0), False)

    def testMedium(self):
        _, temp = genListAndSorted(100)
        value_to_find = random.choice(temp)
        self.assertEqual(binarySearchR(temp, value_to_find), True)

    def testLarge(self):
        _, temp = genListAndSorted(1000)
        value_to_find = random.choice(temp)
        self.assertEqual(binarySearchR(temp, value_to_find), True)

    def testVLarge(self):
        _, temp = genListAndSorted(10000)
        value_to_find = random.choice(temp)
        self.assertEqual(binarySearchR(temp, value_to_find), True)


class TestIterativeBinary(unittest.TestCase):
    def testEmpty(self):
        self.assertEqual(binarySearchI([], 1), False)

    def testOneTrue(self):
        self.assertEqual(binarySearchI([1], 1), True)

    def testOneFalse(self):
        self.assertEqual(binarySearchI([1], 2), False)

    def testTwoTrueOne(self):
        self.assertEqual(binarySearchI([1, 2], 1), True)

    def testTwoTrueTwo(self):
        self.assertEqual(binarySearchI([1, 2], 2), True)

    def testTwoFalse(self):
        self.assertEqual(binarySearchI([1, 2], 3), False)

    def testNegativeTrueNeg(self):
        self.assertEqual(binarySearchI([-2, -1, 0, 1, 2], -2), True)

    def testNegativeTruePos(self):
        self.assertEqual(binarySearchI([-2, -1, 0, 1, 2], 2), True)

    def testNegativeFalse(self):
        self.assertEqual(binarySearchI([-2, -1, 0, 1, 2], 3), False)
    
    def testMiddle(self):
        self.assertEqual(binarySearchI([-2, -1, 0, 1, 2], 0), True)

    def testNonIntTrue(self):
        self.assertEqual(binarySearchI([-2.5, -1.25, 10.89, 231.8], 231.8), True)

    def testNonIntFalse(self):
        self.assertEqual(binarySearchI([-2.5, -1.25, 10.89, 231.8], -11.0), False)

    def testMedium(self):
        _, temp = genListAndSorted(100)
        value_to_find = random.choice(temp)
        self.assertEqual(binarySearchI(temp, value_to_find), True)

    def testLarge(self):
        _, temp = genListAndSorted(1000)
        value_to_find = random.choice(temp)
        self.assertEqual(binarySearchI(temp, value_to_find), True)

    def testVLarge(self):
        _, temp = genListAndSorted(10000)
        value_to_find = random.choice(temp)
        self.assertEqual(binarySearchI(temp, value_to_find), True)


class TestDFS(unittest.TestCase):
    def testEmpty(self):
        self.assertEqual(dfs({}, 1)[0], [])

    def testOne(self):
        self.assertEqual(dfs({1: []}, 1)[0], [1])

    def testDepthTwo(self):
        graph = {1 : [0, 2],
                 2 : [],
                 0 : []}
        self.assertEqual(dfs(graph, 1)[0], [1, 0, 2])

    def testDepthThree(self):
        graph = {1 : [0, 2],
                 2 : [8],
                 0 : [4, 5],
                 4 : [], 
                 5 : [],
                 8 : []}
        self.assertEqual(dfs(graph, 1)[0], [1, 0, 4, 5, 2, 8])

    def testEmpty(self):
        self.assertEqual(dfs({}, 1)[1], False)

    def testOneTrue(self):
        self.assertEqual(dfs({1: []}, 1, 1)[1], True)

    def testOneFalse(self):
        self.assertEqual(dfs({1: []}, 1, 2)[1], False)

    def testDepthTwoTrue(self):
        graph = {1 : [0, 2],
                 2 : [],
                 0 : []}
        self.assertEqual(dfs(graph, 1, 2)[1], True)

    def testDepthTwoFalse(self):
        graph = {1 : [0, 2],
                 2 : [],
                 0 : []}
        self.assertEqual(dfs(graph, 1, 10)[1], False)

    def testDepthThreeTrue(self):
        graph = {1 : [0, 2],
                 2 : [8],
                 0 : [4, 5],
                 4 : [], 
                 5 : [],
                 8 : []}
        self.assertEqual(dfs(graph, 1, 8)[1], True)

    def testDepthThreeFalse(self):
        graph = {1 : [0, 2],
                 2 : [8],
                 0 : [4, 5],
                 4 : [], 
                 5 : [],
                 8 : []}
        self.assertEqual(dfs(graph, 1, 30)[1], False)


class TestBFS(unittest.TestCase):
    def testEmpty(self):
        self.assertEqual(bfs({}, 1)[0], [])

    def testOne(self):
        self.assertEqual(bfs({1: []}, 1)[0], [1])

    def testDepthTwo(self):
        graph = {1 : [0, 2],
                 2 : [],
                 0 : []}
        self.assertEqual(bfs(graph, 1)[0], [1, 0, 2])

    def testDepthThree(self):
        graph = {1 : [0, 2],
                 2 : [8],
                 0 : [4, 5],
                 4 : [], 
                 5 : [],
                 8 : []}
        self.assertEqual(bfs(graph, 1)[0], [1, 0, 2, 4, 5, 8])

    def testEmpty(self):
        self.assertEqual(bfs({}, 1)[1], False)

    def testOneTrue(self):
        self.assertEqual(bfs({1: []}, 1, 1)[1], True)

    def testOneFalse(self):
        self.assertEqual(bfs({1: []}, 1, 2)[1], False)

    def testDepthTwoTrue(self):
        graph = {1 : [0, 2],
                 2 : [],
                 0 : []}
        self.assertEqual(bfs(graph, 1, 2)[1], True)

    def testDepthTwoFalse(self):
        graph = {1 : [0, 2],
                 2 : [],
                 0 : []}
        self.assertEqual(bfs(graph, 1, 10)[1], False)

    def testDepthThreeTrue(self):
        graph = {1 : [0, 2],
                 2 : [8],
                 0 : [4, 5],
                 4 : [], 
                 5 : [],
                 8 : []}
        self.assertEqual(bfs(graph, 1, 8)[1], True)

    def testDepthThreeFalse(self):
        graph = {1 : [0, 2],
                 2 : [8],
                 0 : [4, 5],
                 4 : [], 
                 5 : [],
                 8 : []}
        self.assertEqual(bfs(graph, 1, 30)[1], False)


def testSuite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestRecursiveBinary))
    test_suite.addTest(unittest.makeSuite(TestIterativeBinary))
    test_suite.addTest(unittest.makeSuite(TestDFS))
    test_suite.addTest(unittest.makeSuite(TestBFS))
    return test_suite

if __name__ == '__main__':
    suite = testSuite()
    runner = unittest.TextTestRunner()
    runner.run(suite)