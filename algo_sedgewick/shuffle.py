#!/usr/bin/python2

import random
from elementary_sort import swap

class KnuthShuffle:
    @staticmethod
    def Shuffle(arr, len):
        for iter in range(len):
            rand = random.randint(0, iter)
            swap(arr, iter, rand)
            

