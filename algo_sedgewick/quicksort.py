#!/usr/bin/python2

from elementary_sort import swap

class QSort3Way:
    @staticmethod
    def _sortOnce(arr, start, end):
        if start >= end: return
        lo, hi = start, end
        lt, gt = lo, hi
        i, v = start, arr[lo]
        while i <= gt:
            if arr[i] < v:
                swap(arr, i, lt)
                i += 1
                lt += 1
            elif arr[i] > v:
                swap(arr, i, gt)
                gt -= 1
            else:
                i += 1

        QSort3Way._sortOnce(arr, start, lt - 1)
        QSort3Way._sortOnce(arr, gt + 1, end)
        return i

    @staticmethod
    def Sort(arr, len):
        QSort3Way._sortOnce(arr, 0, len - 1)


