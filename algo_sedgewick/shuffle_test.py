#!/usr/bin/python2

import unittest
from shuffle import KnuthShuffle

class TestShuffle(unittest.TestCase):
    def setUp(self):
        print '\nRun test for Shuffle'

    def test_shuffle(self):
        TOTAL_TESTS, EPSILON = 100000, 0.01
        stat = dict([])
        for i in [x * 10 for x in range(10)]:
            stat[i] = [0] * 10

        for test_cases in range(TOTAL_TESTS):
            l = [x * 10 for x in range(10)]
            KnuthShuffle.Shuffle(l, 10)
            for pos in range(10):
                stat[l[pos]][pos] = stat[l[pos]][pos] + 1

        # check uniform distribution
        for num in stat:
            for pos in range(10):
                prob = stat[num][pos] * 1.0 / TOTAL_TESTS
                self.assertTrue(abs(prob - 0.1)< EPSILON)

if __name__ == '__main__':
    unittest.main()

