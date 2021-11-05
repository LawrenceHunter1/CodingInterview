import unittest, random

import sys
sys.path.append("../")
from Sorts.Quick import quickSortHandler as quickSort
from Sorts.Bubble import bubbleSort, bubbleSortOpt
from Sorts.Merge import mergeSort
from Sorts.Insertion import insertionSort
from Sorts.Selection import selectionSort
from Sorts.Heap import heapSort
from Sorts.Radix import radixSort
from Sorts.Bucket import bucketSort

def genList(size):
        return [random.randint(0, 100) for _ in range(size)]

def genListAndSorted(size):
    temp = genList(size)
    temp_sorted = temp
    temp_sorted.sort()
    return temp, temp_sorted

class TestQuickSort(unittest.TestCase):

    def testEmpty(self):
        self.assertEqual(quickSort([]), [])

    def testOneItem(self):
        self.assertEqual(quickSort([1]), [1])

    def testTwoItemsSorted(self):
        self.assertEqual(quickSort([1, 2]), [1, 2])

    def testTwoItemsUnsorted(self):
        self.assertEqual(quickSort([2, 1]), [1, 2])

    def testSorted(self):
        self.assertEqual(quickSort([1, 2, 3, 4]), [1, 2, 3, 4])
    
    def testTwoWrong(self):
        self.assertEqual(quickSort([1, 3, 2, 4]), [1, 2, 3, 4])

    def testThreeWrong(self):
        self.assertEqual(quickSort([3, 2, 1, 4]), [1, 2, 3, 4])
    
    def testReverseWrong(self):
        self.assertEqual(quickSort([4, 3, 2, 1]), [1, 2, 3, 4])

    def testSmall(self):
        l, l_sorted = genListAndSorted(10)
        self.assertEqual(quickSort(l), l_sorted)

    def testMed(self):
        l, l_sorted = genListAndSorted(100)
        self.assertEqual(quickSort(l), l_sorted)

    def testLarge(self):
        l, l_sorted = genListAndSorted(1000)
        self.assertEqual(quickSort(l), l_sorted)

    def testVLarge(self):
        l, l_sorted = genListAndSorted(10000)
        self.assertEqual(quickSort(l), l_sorted)


class TestBubbleSort(unittest.TestCase):

    def testEmpty(self):
        self.assertEqual(bubbleSort([]), [])

    def testOneItem(self):
        self.assertEqual(bubbleSort([1]), [1])

    def testTwoItemsSorted(self):
        self.assertEqual(bubbleSort([1, 2]), [1, 2])

    def testTwoItemsUnsorted(self):
        self.assertEqual(bubbleSort([2, 1]), [1, 2])

    def testSorted(self):
        self.assertEqual(bubbleSort([1, 2, 3, 4]), [1, 2, 3, 4])
    
    def testTwoWrong(self):
        self.assertEqual(bubbleSort([1, 3, 2, 4]), [1, 2, 3, 4])

    def testThreeWrong(self):
        self.assertEqual(bubbleSort([3, 2, 1, 4]), [1, 2, 3, 4])
    
    def testReverseWrong(self):
        self.assertEqual(bubbleSort([4, 3, 2, 1]), [1, 2, 3, 4])

    def testSmall(self):
        l, l_sorted = genListAndSorted(10)
        self.assertEqual(bubbleSort(l), l_sorted)

    def testMed(self):
        l, l_sorted = genListAndSorted(100)
        self.assertEqual(bubbleSort(l), l_sorted)

    def testLarge(self):
        l, l_sorted = genListAndSorted(1000)
        self.assertEqual(bubbleSort(l), l_sorted)


class TestBubbleSortOpt(unittest.TestCase):

    def testEmpty(self):
        self.assertEqual(bubbleSortOpt([]), [])

    def testOneItem(self):
        self.assertEqual(bubbleSortOpt([1]), [1])

    def testTwoItemsSorted(self):
        self.assertEqual(bubbleSortOpt([1, 2]), [1, 2])

    def testTwoItemsUnsorted(self):
        self.assertEqual(bubbleSortOpt([2, 1]), [1, 2])

    def testSorted(self):
        self.assertEqual(bubbleSortOpt([1, 2, 3, 4]), [1, 2, 3, 4])
    
    def testTwoWrong(self):
        self.assertEqual(bubbleSortOpt([1, 3, 2, 4]), [1, 2, 3, 4])

    def testThreeWrong(self):
        self.assertEqual(bubbleSortOpt([3, 2, 1, 4]), [1, 2, 3, 4])
    
    def testReverseWrong(self):
        self.assertEqual(bubbleSortOpt([4, 3, 2, 1]), [1, 2, 3, 4])

    def testSmall(self):
        l, l_sorted = genListAndSorted(10)
        self.assertEqual(bubbleSortOpt(l), l_sorted)

    def testMed(self):
        l, l_sorted = genListAndSorted(100)
        self.assertEqual(bubbleSortOpt(l), l_sorted)

    def testLarge(self):
        l, l_sorted = genListAndSorted(1000)
        self.assertEqual(bubbleSortOpt(l), l_sorted)


class TestMergeSort(unittest.TestCase):

    def testEmpty(self):
        self.assertEqual(mergeSort([]), [])

    def testOneItem(self):
        self.assertEqual(mergeSort([1]), [1])

    def testTwoItemsSorted(self):
        self.assertEqual(mergeSort([1, 2]), [1, 2])

    def testTwoItemsUnsorted(self):
        self.assertEqual(mergeSort([2, 1]), [1, 2])

    def testSorted(self):
        self.assertEqual(mergeSort([1, 2, 3, 4]), [1, 2, 3, 4])
    
    def testTwoWrong(self):
        self.assertEqual(mergeSort([1, 3, 2, 4]), [1, 2, 3, 4])

    def testThreeWrong(self):
        self.assertEqual(mergeSort([3, 2, 1, 4]), [1, 2, 3, 4])
    
    def testReverseWrong(self):
        self.assertEqual(mergeSort([4, 3, 2, 1]), [1, 2, 3, 4])

    def testSmall(self):
        l, l_sorted = genListAndSorted(10)
        self.assertEqual(mergeSort(l), l_sorted)

    def testMed(self):
        l, l_sorted = genListAndSorted(100)
        self.assertEqual(mergeSort(l), l_sorted)

    def testLarge(self):
        l, l_sorted = genListAndSorted(1000)
        self.assertEqual(mergeSort(l), l_sorted)

    def testVLarge(self):
        l, l_sorted = genListAndSorted(10000)
        self.assertEqual(mergeSort(l), l_sorted)


class TestInsertionSort(unittest.TestCase):

    def testEmpty(self):
        self.assertEqual(insertionSort([]), [])

    def testOneItem(self):
        self.assertEqual(insertionSort([1]), [1])

    def testTwoItemsSorted(self):
        self.assertEqual(insertionSort([1, 2]), [1, 2])

    def testTwoItemsUnsorted(self):
        self.assertEqual(insertionSort([2, 1]), [1, 2])

    def testSorted(self):
        self.assertEqual(insertionSort([1, 2, 3, 4]), [1, 2, 3, 4])
    
    def testTwoWrong(self):
        self.assertEqual(insertionSort([1, 3, 2, 4]), [1, 2, 3, 4])

    def testThreeWrong(self):
        self.assertEqual(insertionSort([3, 2, 1, 4]), [1, 2, 3, 4])
    
    def testReverseWrong(self):
        self.assertEqual(insertionSort([4, 3, 2, 1]), [1, 2, 3, 4])

    def testSmall(self):
        l, l_sorted = genListAndSorted(10)
        self.assertEqual(insertionSort(l), l_sorted)

    def testMed(self):
        l, l_sorted = genListAndSorted(100)
        self.assertEqual(insertionSort(l), l_sorted)

    def testLarge(self):
        l, l_sorted = genListAndSorted(1000)
        self.assertEqual(insertionSort(l), l_sorted)


class TestSelectionSort(unittest.TestCase):

    def testEmpty(self):
        self.assertEqual(selectionSort([]), [])

    def testOneItem(self):
        self.assertEqual(selectionSort([1]), [1])

    def testTwoItemsSorted(self):
        self.assertEqual(selectionSort([1, 2]), [1, 2])

    def testTwoItemsUnsorted(self):
        self.assertEqual(selectionSort([2, 1]), [1, 2])

    def testSorted(self):
        self.assertEqual(selectionSort([1, 2, 3, 4]), [1, 2, 3, 4])
    
    def testTwoWrong(self):
        self.assertEqual(selectionSort([1, 3, 2, 4]), [1, 2, 3, 4])

    def testThreeWrong(self):
        self.assertEqual(selectionSort([3, 2, 1, 4]), [1, 2, 3, 4])
    
    def testReverseWrong(self):
        self.assertEqual(selectionSort([4, 3, 2, 1]), [1, 2, 3, 4])

    def testSmall(self):
        l, l_sorted = genListAndSorted(10)
        self.assertEqual(selectionSort(l), l_sorted)

    def testMed(self):
        l, l_sorted = genListAndSorted(100)
        self.assertEqual(selectionSort(l), l_sorted)

    def testLarge(self):
        l, l_sorted = genListAndSorted(1000)
        self.assertEqual(selectionSort(l), l_sorted)


class TestHeapSort(unittest.TestCase):

    def testEmpty(self):
        self.assertEqual(heapSort([]), [])

    def testOneItem(self):
        self.assertEqual(heapSort([1]), [1])

    def testTwoItemsSorted(self):
        self.assertEqual(heapSort([1, 2]), [1, 2])

    def testTwoItemsUnsorted(self):
        self.assertEqual(heapSort([2, 1]), [1, 2])

    def testSorted(self):
        self.assertEqual(heapSort([1, 2, 3, 4]), [1, 2, 3, 4])
    
    def testTwoWrong(self):
        self.assertEqual(heapSort([1, 3, 2, 4]), [1, 2, 3, 4])

    def testThreeWrong(self):
        self.assertEqual(heapSort([3, 2, 1, 4]), [1, 2, 3, 4])
    
    def testReverseWrong(self):
        self.assertEqual(heapSort([4, 3, 2, 1]), [1, 2, 3, 4])

    def testSmall(self):
        l, l_sorted = genListAndSorted(10)
        self.assertEqual(heapSort(l), l_sorted)

    def testMed(self):
        l, l_sorted = genListAndSorted(100)
        self.assertEqual(heapSort(l), l_sorted)

    def testLarge(self):
        l, l_sorted = genListAndSorted(1000)
        self.assertEqual(heapSort(l), l_sorted)

    def testVLarge(self):
        l, l_sorted = genListAndSorted(10000)
        self.assertEqual(heapSort(l), l_sorted)


class TestRadixSort(unittest.TestCase):

    def testEmpty(self):
        self.assertEqual(radixSort([]), [])

    def testOneItem(self):
        self.assertEqual(radixSort([1]), [1])

    def testTwoItemsSorted(self):
        self.assertEqual(radixSort([1, 2]), [1, 2])

    def testTwoItemsUnsorted(self):
        self.assertEqual(radixSort([2, 1]), [1, 2])

    def testSorted(self):
        self.assertEqual(radixSort([1, 2, 3, 4]), [1, 2, 3, 4])
    
    def testTwoWrong(self):
        self.assertEqual(radixSort([1, 3, 2, 4]), [1, 2, 3, 4])

    def testThreeWrong(self):
        self.assertEqual(radixSort([3, 2, 1, 4]), [1, 2, 3, 4])
    
    def testReverseWrong(self):
        self.assertEqual(radixSort([4, 3, 2, 1]), [1, 2, 3, 4])

    def testSmall(self):
        l, l_sorted = genListAndSorted(10)
        self.assertEqual(radixSort(l), l_sorted)

    def testMed(self):
        l, l_sorted = genListAndSorted(100)
        self.assertEqual(radixSort(l), l_sorted)

    def testLarge(self):
        l, l_sorted = genListAndSorted(1000)
        self.assertEqual(radixSort(l), l_sorted)

    def testVLarge(self):
        l, l_sorted = genListAndSorted(10000)
        self.assertEqual(radixSort(l), l_sorted)


class TestBucketSort(unittest.TestCase):

    def testEmpty(self):
        self.assertEqual(bucketSort([]), [])

    def testOneItem(self):
        self.assertEqual(bucketSort([1]), [1])

    def testTwoItemsSorted(self):
        self.assertEqual(bucketSort([1, 2]), [1, 2])

    def testTwoItemsUnsorted(self):
        self.assertEqual(bucketSort([2, 1]), [1, 2])

    def testSorted(self):
        self.assertEqual(bucketSort([1, 2, 3, 4]), [1, 2, 3, 4])
    
    def testTwoWrong(self):
        self.assertEqual(bucketSort([1, 3, 2, 4]), [1, 2, 3, 4])

    def testThreeWrong(self):
        self.assertEqual(bucketSort([3, 2, 1, 4]), [1, 2, 3, 4])
    
    def testReverseWrong(self):
        self.assertEqual(bucketSort([4, 3, 2, 1]), [1, 2, 3, 4])

    def testSmall(self):
        l, l_sorted = genListAndSorted(10)
        self.assertEqual(bucketSort(l), l_sorted)

    def testMed(self):
        l, l_sorted = genListAndSorted(100)
        self.assertEqual(bucketSort(l), l_sorted)

    def testLarge(self):
        l, l_sorted = genListAndSorted(1000)
        self.assertEqual(bucketSort(l), l_sorted)


def testSuite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestQuickSort))
    test_suite.addTest(unittest.makeSuite(TestBubbleSort))
    test_suite.addTest(unittest.makeSuite(TestBubbleSortOpt))
    test_suite.addTest(unittest.makeSuite(TestMergeSort))
    test_suite.addTest(unittest.makeSuite(TestInsertionSort))
    test_suite.addTest(unittest.makeSuite(TestSelectionSort))
    test_suite.addTest(unittest.makeSuite(TestHeapSort))
    test_suite.addTest(unittest.makeSuite(TestRadixSort))
    test_suite.addTest(unittest.makeSuite(TestBucketSort))
    return test_suite

if __name__ == '__main__':
    suite = testSuite()
    runner = unittest.TextTestRunner()
    runner.run(suite)