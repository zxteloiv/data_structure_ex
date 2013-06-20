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
