#!/usr/bin/python2

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = arr[i]

# 1. selection sort
# During each iteration, select the minimum and swap to the most left
def SelectionSort(arr, len):
    for iter in range(len):
        min_pos = iter
        for pos in range(min_pos + 1, len):
            if arr[pos] < arr[min_pos]:
                min_pos = pos
        swap(arr, iter, min_pos)

# 2. insertion sort
# During each iteration, swap the number with its left number
def InsertionSort(arr, len):
    for iter in range(len):
        for move_pos in range(iter, 0, -1):
            if arr[move_pos] < arr[move_pos - 1]:
                swap(arr, move_pos, move_pos - 1)
            else:
                break

# 3. shell sort
# Unlike insertion sort moves the element 1 position to left,
# shell sort moves k positions each time
class ShellSort:
    """
    An h-sorted array is h interleaved sorted sequences.
    H-Sort is actually an insertion sort
    """
    @staticmethod
    def _h_sort(h, arr, len):
        for iter in range(h, len):
            for move_pos in range(iter, 0, -h):
                if arr[move_pos] < arr[move_pos - h]:
                    swap(arr, move_pos, move_pos - h)
                else:
                    break

    """
    Manually choose descending values of h's
    Here we choose h(t) = 3*h(t-1) + 1; h(0) = 1
    When h=1, h-sort is just identitical to insertion sort
    """
    @staticmethod
    def Sort(arr, len):
        h = 1
        # just ensure h-sort could move 2~3 items per iteration
        while h < len / 3:
            h = h * 3 + 1
        while h >= 1:
            ShellSort._h_sort(h, arr, len)
            h = h / 3
