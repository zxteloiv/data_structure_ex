#!/usr/bin/python2

from elementary_sort import swap

# 1. Unordered using array
class UnorderedPriorityQueue:
    def __init__(self):
        self.arr = []

    def Insert(self, key):
        self.arr.append(key)
        print self.arr

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

