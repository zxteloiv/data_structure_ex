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

class QSort:
    @staticmethod
    def _partition(arr, start, end):
        cur1, cur2 = start, end
        while True:
            while cur1 <= end and arr[cur1] < arr[start]: cur1 += 1
            while cur2 >= start and arr[cur2] > arr[start]: cur2 -= 1
            if cur1 >= cur2: break
            swap(arr, cur1, cur2)
            cur1 += 1
            cur2 -= 1

        swap(arr, cur2, start)
        return cur2

    @staticmethod
    def _sort(arr, start, end):
        if start >= end: return
        pos = QSort._partition(arr, start, end)
        QSort._sort(arr, start, pos - 1)
        QSort._sort(arr, pos + 1, end)

    @staticmethod
    def Sort(arr, len):
        QSort._sort(arr, 0, len - 1)

