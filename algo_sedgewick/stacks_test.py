#!/usr/bin/python2

import unittest
from stacks import ListStack

class TestListStack(unittest.TestCase):
    def setUp(self):
        #print 'Run test setUp method...'
        pass

    def test_init(self):
        s = ListStack()

    def test_empty(self):
        s = ListStack()
        self.assertTrue(s.IsEmpty())

    def test_push(self):
        s = ListStack()
        s.Push(10)
        self.assertTrue(not s.IsEmpty())
        s.Push(20)
        self.assertTrue(not s.IsEmpty())
        s.Push(30).Push(40)
        self.assertTrue(not s.IsEmpty())

    def test_pop(self):
        s = ListStack()
        self.assertEqual(s.Pop(), None)
        self.assertTrue(s.IsEmpty())
        s.Push(10)
        self.assertTrue(not s.IsEmpty())
        self.assertEqual(s.Pop(), 10)
        self.assertTrue(s.IsEmpty())
        s.Push(10)
        self.assertTrue(not s.IsEmpty())
        s.Push(20)
        self.assertTrue(not s.IsEmpty())
        s.Push(30)
        self.assertEqual(s.Pop(), 30)
        self.assertTrue(not s.IsEmpty())
        s.Push(40)
        self.assertEqual(s.Pop(), 40)
        self.assertTrue(not s.IsEmpty())
        self.assertEqual(s.Pop(), 20)
        self.assertTrue(not s.IsEmpty())
        self.assertEqual(s.Pop(), 10)
        self.assertEqual(s.Pop(), None)
        self.assertTrue(s.IsEmpty())
        
if __name__ == '__main__':
    unittest.main()
