from elementary_sort import swap
from priority_queue import BinaryHeapPQ

# 1. A in-place implementation of heapsort
# First build heap
# Second del
class HeapSort:
    @staticmethod
    def _sink(arr, pos, end):
        while pos * 2 <= end:
            ch = pos * 2
            if (ch + 1) <= end and arr[ch] < arr[ch + 1]:
                ch = ch + 1
            if arr[pos] < arr[ch]: swap(arr, pos, ch)
            else: break
            pos = ch

    @staticmethod
    def Sort(arr, len):
        end = len - 1
        for k in range(end / 2, 0, -1):
            HeapSort._sink(arr, k, end)
        while end > 1:
            swap(arr, 1, end)
            end -= 1
            HeapSort._sink(arr, 1, end)

class SimpleHeapSort:
    @staticmethod
    def Sort(arr, len):
        pq = BinaryHeapPQ()
        for i in range(len): pq.Insert(arr[i])
        for i in range(len - 1, -1, -1): arr[i] = pq.DelMax()
            
        
