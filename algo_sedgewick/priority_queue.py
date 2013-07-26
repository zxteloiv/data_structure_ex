#!/usr/bin/python2

from elementary_sort import swap

# 1. Unordered using array
class UnorderedPriorityQueue:
    def __init__(self):
        self.arr = []

    def Insert(self, key):
        self.arr.append(key)

    def DelMax(self):
        if self.Size() == 0: return None
        max_val, max_pos = None, 0
        for (i,val) in enumerate(self.arr):
            if i == 0: max_val, max_pos = self.arr[i], i
            elif val > max_val: max_val, max_pos = val, i
        swap(self.arr, max_pos, self.Size() - 1)
        return self.arr.pop()

    def IsEmpty(self):
        return self.Size() == 0

    def Size(self):
        return len(self.arr)

# 2. implement using binary heap
#
# A binary heap is a binary tree in which a parent node is greater
# than its children, and its 2 children have no need to be ordered.
#
# Here we implement it using an array, if start using index from 1,
# then root is at 1, the k's parent is as k/2, and k's children are
# at 2k and 2k+1
#
class BinaryHeapPQ:
    def __init__(self):
        # arr[0] is reserved and not used, this is an empty heap
        self.arr = [ 0 ]

    def _swim(self, pos):
        """
        _swim: check if a position is greater than its parent,
               if so, exchange them and keep comparing the new
               parent with its own parent
        """
        while pos > 1 and self.arr[pos] > self.arr[pos / 2]:
            swap(self.arr, pos, pos / 2)
            pos = pos / 2

    def _sink(self, pos):
        """
        _sink: check if a position is less than its children,
               if so, exchange it with the greater child then
               keep comparing the new child with its children
        """
        last_id = len(self.arr) - 1
        while pos * 2 <= last_id:
            ch = pos * 2        # select child left
            if (ch + 1) <= last_id and self.arr[ch] < self.arr[ch + 1]:
                ch = ch + 1     # select right greater child if it exists
            if self.arr[pos] < self.arr[ch]: swap(self.arr, pos, ch)
            else: break
            pos = ch

    def Insert(self, key):
        self.arr.append(key)
        self._swim(len(self.arr) - 1)

    def DelMax(self):
        if self.IsEmpty(): return None
        swap(self.arr, 1, len(self.arr) - 1)
        key = self.arr.pop()
        self._sink(1)
        return key

    def IsEmpty(self):
        return len(self.arr) == 1

    def Size(self):
        return len(self.arr) - 1
