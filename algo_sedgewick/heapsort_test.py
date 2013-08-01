#!/usr/bin/python2

import unittest
from heapsort import HeapSort, SimpleHeapSort
from random import sample
from elementary_sort_test import SortTester

class TestHeapSort(SortTester):
    def setUp(self):
        print "\nRun test for HeapSort"

    def test_sort(self):
        arr = range(10)
        SimpleHeapSort.Sort(arr, len(arr))
        print arr
        self.checkArrayAscending(arr)
        arr = [20, 18, 17, 16, 15, 14, 13, 12, 11, 10]
        SimpleHeapSort.Sort(arr, len(arr))
        print arr
        self.checkArrayAscending(arr)
        arr = [10, 20, 30, 40, 50, 11, 22, 33, 44, 55]
        SimpleHeapSort.Sort(arr, len(arr))
        print arr
        self.checkArrayAscending(arr)
        arr = [10, 20, 10, 40, 10, 11, 22, 10, 44, 10]
        SimpleHeapSort.Sort(arr, len(arr))
        print arr
        self.checkArrayAscending(arr)
        arr = sample(range(1,100), 20)
        arr.extend([50] * 10)
        SimpleHeapSort.Sort(arr, len(arr))
        print arr
        self.checkArrayAscending(arr)

if __name__ == '__main__':
    unittest.main()

