#!/usr/bin/python2

import unittest
from binary_search_tree import BST

class TestBST(unittest.TestCase):
    def setUp(self):
        print '\nRun test for BinarySearchTree'

    def test_init(self):
        bst = BST()
        self.assertEqual(bst.Size(), 0)
        bst.Put('a', 1)
        self.assertEqual(bst.Size(), 1)
        self.assertEqual(bst.Get('a'), 1)
        bst.Put('ab', 2)
        self.assertEqual(bst.Size(), 2)
        self.assertEqual(bst.Get('ab'), 2)
        bst.Put('a', 3)
        self.assertEqual(bst.Size(), 2)
        self.assertEqual(bst.Get('a'), 3)

        
if __name__ == '__main__':
    unittest.main()


