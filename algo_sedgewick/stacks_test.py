#!/usr/bin/python2

import unittest
from stacks import ListStack, ArrayStack, Stack

class TestListStack(unittest.TestCase):
    def setUp(self):
        print '\nRun test for ListStack'

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

    def test_size(self):
        s = ListStack()
        self.assertEqual(s.Size(), 0)
        s.Push(10)
        self.assertEqual(s.Size(), 1)
        s.Pop()
        self.assertEqual(s.Size(), 0)
        s.Push(10)
        s.Push(10)
        s.Push(10)
        self.assertEqual(s.Size(), 3)
        s.Push(10)
        self.assertEqual(s.Size(), 4)
        s.Pop()
        self.assertEqual(s.Size(), 3)
        s.Pop()
        self.assertEqual(s.Size(), 2)
        s.Pop()
        self.assertEqual(s.Size(), 1)
        s.Pop()
        self.assertEqual(s.Size(), 0)

class TestArrayStack(unittest.TestCase):
    def setUp(self):
        print '\nRun test for ArrayStack'

    def test_init(self):
        s = ArrayStack(20)
        l = ArrayStack()

    def test_empty(self):
        s = ArrayStack(20)
        l = ArrayStack()
        self.assertTrue(s.IsEmpty())
        self.assertTrue(l.IsEmpty())

    def test_push(self):
        s = ArrayStack(5)
        s.Push(100)
        self.assertTrue(not s.IsEmpty())
        s.Push(200)
        self.assertTrue(not s.IsEmpty())
        s.Push(300).Push(400)
        self.assertTrue(not s.IsEmpty())

    def test_pop(self):
        s = ArrayStack()
        self.assertTrue(s.IsEmpty())
        self.assertEqual(s.Pop(), None)
        s.Push(10)
        self.assertTrue(not s.IsEmpty())
        self.assertEqual(s.Pop(), 10)
        s.Push(10).Push(20).Push(30)
        self.assertEqual(s.Pop(), 30)
        s.Push(40)
        self.assertEqual(s.Pop(), 40)
        self.assertTrue(not s.IsEmpty())
        self.assertEqual(s.Pop(), 20)
        self.assertTrue(not s.IsEmpty())
        self.assertEqual(s.Pop(), 10)
        self.assertTrue(s.IsEmpty())
        self.assertEqual(s.Pop(), None)

    def test_size(self):
        s = ArrayStack()
        self.assertEqual(s.Size(), 0)
        s.Push(10)
        self.assertEqual(s.Size(), 1)
        s.Push(10)
        self.assertEqual(s.Size(), 2)
        self.assertEqual(s.Pop(), 10)
        self.assertEqual(s.Size(), 1)
        self.assertEqual(s.Pop(), 10)
        self.assertEqual(s.Size(), 0)

    def test_reserved_size(self):
        s = ArrayStack()
        self.assertEqual(s.ReservedSize(), 10)
        s = ArrayStack(20)
        self.assertEqual(s.ReservedSize(), 20)
        s = ArrayStack(5)
        self.assertEqual(s.ReservedSize(), 5)
        s.Push(10).Push(20)
        self.assertEqual(s.ReservedSize(), 5)
        s.Push(30).Push(40)
        self.assertEqual(s.ReservedSize(), 5)
        s.Push(50)
        self.assertEqual(s.ReservedSize(), 10)
        s.Push(60)
        self.assertEqual(s.ReservedSize(), 10)
        s.Push(70).Push(80).Push(90).Push(100)
        self.assertEqual(s.ReservedSize(), 20)
        s.Pop(); s.Pop(); s.Pop(); s.Pop();
        self.assertEqual(s.ReservedSize(), 20)
        s.Pop()
        self.assertEqual(s.ReservedSize(), 10)
        s.Pop()
        self.assertEqual(s.ReservedSize(), 10)
        s.Pop(); s.Pop(); s.Pop(); s.Pop();
        self.assertEqual(s.ReservedSize(), 10)
        self.assertEqual(s.Pop(), None)

class TestStack(unittest.TestCase):
    def setUp(self):
        print "\nRun test for Stack"
        
    def test_stack(self):
        s = Stack()
        self.assertTrue(s.IsEmpty())
        self.assertEqual(s.Size(), 0)
        self.assertEqual(s.Pop(), None)
        s.Push(10)
        self.assertTrue(not s.IsEmpty())
        self.assertEqual(s.Size(), 1)
        self.assertEqual(s.Pop(), 10)
        self.assertEqual(s.Size(), 0)
        self.assertEqual(s.Pop(), None)
        self.assertTrue(s.IsEmpty())
        s.Push(10).Push(20)
        self.assertTrue(not s.IsEmpty())
        self.assertEqual(s.Size(), 2)
        s.Push(30).Push(40)
        self.assertTrue(not s.IsEmpty())
        self.assertEqual(s.Size(), 4)
        self.assertEqual(s.Pop(), 40)
        self.assertEqual(s.Size(), 3)
        self.assertTrue(not s.IsEmpty())
        self.assertEqual(s.Pop(), 30)
        self.assertEqual(s.Size(), 2)
        self.assertTrue(not s.IsEmpty())
        self.assertEqual(s.Pop(), 20)
        self.assertEqual(s.Size(), 1)
        self.assertTrue(not s.IsEmpty())
        self.assertEqual(s.Pop(), 10)
        self.assertEqual(s.Size(), 0)
        self.assertTrue(s.IsEmpty())
        self.assertEqual(s.Pop(), None)

if __name__ == '__main__':
    unittest.main()
