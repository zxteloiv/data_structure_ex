#!/usr/bin/python2

import unittest
from elementary_sort import SelectionSort, InsertionSort, ShellSort
from random import sample


class TestSelectionSort(unittest.TestCase):
    def setUp(self):
        print "\nRun test for SelectionSort"

    def checkArrayAscending(self, arr):
        for pos in range(1, len(arr)):
            self.assertTrue(arr[pos - 1] <= arr[pos])

    def test_sort(self):
        arr = range(10)
        SelectionSort(arr, len(arr))
        self.checkArrayAscending(arr)
        arr = [20, 18, 17, 16, 15, 14, 13, 12, 11, 10]
        SelectionSort(arr, len(arr))
        self.checkArrayAscending(arr)
        arr = [10, 20, 30, 40, 50, 11, 22, 33, 44, 55]
        SelectionSort(arr, len(arr))
        self.checkArrayAscending(arr)
        arr = sample(range(1,100), 20)
        SelectionSort(arr, len(arr))
        self.checkArrayAscending(arr)

class TestInsertionSort(unittest.TestCase):
    def setUp(self):
        print "\nRun test for InsertionSort"

    def checkArrayAscending(self, arr):
        for pos in range(1, len(arr)):
            self.assertTrue(arr[pos - 1] <= arr[pos])

    def test_sort(self):
        arr = range(10)
        InsertionSort(arr, len(arr))
        self.checkArrayAscending(arr)
        arr = [20, 18, 17, 16, 15, 14, 13, 12, 11, 10]
        InsertionSort(arr, len(arr))
        self.checkArrayAscending(arr)
        arr = [10, 20, 30, 40, 50, 11, 22, 33, 44, 55]
        InsertionSort(arr, len(arr))
        self.checkArrayAscending(arr)
        arr = sample(range(1,100), 20)
        InsertionSort(arr, len(arr))
        self.checkArrayAscending(arr)

class TestShellSort(unittest.TestCase):
    def setUp(self):
        print "\nRun test for ShellSort"

    def checkArrayAscending(self, arr):
        for pos in range(1, len(arr)):
            self.assertTrue(arr[pos - 1] <= arr[pos])

    def test_sort(self):
        arr = range(10)
        ShellSort.Sort(arr, len(arr))
        self.checkArrayAscending(arr)
        arr = [20, 18, 17, 16, 15, 14, 13, 12, 11, 10]
        ShellSort.Sort(arr, len(arr))
        self.checkArrayAscending(arr)
        arr = [10, 20, 30, 40, 50, 11, 22, 33, 44, 55]
        ShellSort.Sort(arr, len(arr))
        self.checkArrayAscending(arr)
        arr = sample(range(1,100), 20)
        ShellSort.Sort(arr, len(arr))
        self.checkArrayAscending(arr)

if __name__ == '__main__':
    unittest.main()


