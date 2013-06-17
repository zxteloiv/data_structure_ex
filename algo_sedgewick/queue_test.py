#!/usr/bin/python2

import unittest
from queue import ListQueue, ArrayQueue, Queue

class TestListQueue(unittest.TestCase):
    def setUp(self):
        print '\nRun test for ListQueue'

    def test_init(self):
        q = ListQueue()

    def test_empty(self):
        q = ListQueue()
        self.assertTrue(q.IsEmpty())

    def test_enqueue(self):
        q = ListQueue()
        q.Enqueue(10)
        self.assertTrue(not q.IsEmpty())
        q.Enqueue(20)
        self.assertTrue(not q.IsEmpty())
        q.Enqueue(30).Enqueue(40)
        self.assertTrue(not q.IsEmpty())

    def test_dequeue(self):
        q = ListQueue()
        self.assertEqual(q.Dequeue(), None)
        self.assertTrue(q.IsEmpty())
        q.Enqueue(10)
        self.assertTrue(not q.IsEmpty())
        self.assertEqual(q.Dequeue(), 10)
        self.assertTrue(q.IsEmpty())
        q.Enqueue(10)
        self.assertTrue(not q.IsEmpty())
        q.Enqueue(20)
        self.assertTrue(not q.IsEmpty())
        q.Enqueue(30)
        self.assertEqual(q.Dequeue(), 10)
        self.assertTrue(not q.IsEmpty())
        q.Enqueue(40)
        self.assertEqual(q.Dequeue(), 20)
        self.assertTrue(not q.IsEmpty())
        self.assertEqual(q.Dequeue(), 30)
        self.assertTrue(not q.IsEmpty())
        self.assertEqual(q.Dequeue(), 40)
        self.assertTrue(q.IsEmpty())
        self.assertEqual(q.Dequeue(), None)

    def test_size(self):
        q = ListQueue()
        self.assertEqual(q.Size(), 0)
        q.Enqueue(10)
        self.assertEqual(q.Size(), 1)
        q.Dequeue()
        self.assertEqual(q.Size(), 0)
        q.Enqueue(10)
        q.Enqueue(10)
        q.Enqueue(10)
        self.assertEqual(q.Size(), 3)
        q.Enqueue(10)
        self.assertEqual(q.Size(), 4)
        q.Dequeue()
        self.assertEqual(q.Size(), 3)
        q.Dequeue()
        self.assertEqual(q.Size(), 2)
        q.Dequeue()
        self.assertEqual(q.Size(), 1)
        q.Dequeue()
        self.assertEqual(q.Size(), 0)

class TestArrayQueue(unittest.TestCase):
    def setUp(self):
        print '\nRun test for ArrayQueue\n'

    def test_init(self):
        q = ArrayQueue(20)
        l = ArrayQueue()

    def test_empty(self):
        q = ArrayQueue(20)
        l = ArrayQueue()
        self.assertTrue(q.IsEmpty())
        self.assertTrue(l.IsEmpty())

    def test_enqueue(self):
        q = ArrayQueue(5)
        q.Enqueue(100)
        self.assertTrue(not q.IsEmpty())
        q.Enqueue(200)
        self.assertTrue(not q.IsEmpty())
        q.Enqueue(300).Enqueue(400)
        self.assertTrue(not q.IsEmpty())

    def test_dequeue(self):
        q = ArrayQueue()
        self.assertTrue(q.IsEmpty())
        self.assertEqual(q.Dequeue(), None)
        q.Enqueue(10)
        self.assertTrue(not q.IsEmpty())
        self.assertEqual(q.Dequeue(), 10)
        q.Enqueue(10).Enqueue(20).Enqueue(30)
        self.assertEqual(q.Dequeue(), 10)
        q.Enqueue(40)
        self.assertEqual(q.Dequeue(), 20)
        self.assertTrue(not q.IsEmpty())
        self.assertEqual(q.Dequeue(), 30)
        self.assertTrue(not q.IsEmpty())
        self.assertEqual(q.Dequeue(), 40)
        self.assertTrue(q.IsEmpty())
        self.assertEqual(q.Dequeue(), None)

    def test_size(self):
        q = ArrayQueue()
        self.assertEqual(q.Size(), 0)
        q.Enqueue(10)
        self.assertEqual(q.Size(), 1)
        q.Enqueue(10)
        self.assertEqual(q.Size(), 2)
        self.assertEqual(q.Dequeue(), 10)
        self.assertEqual(q.Size(), 1)
        self.assertEqual(q.Dequeue(), 10)
        self.assertEqual(q.Size(), 0)

    def test_reserved_size(self):
        q = ArrayQueue()
        self.assertEqual(q.ReservedSize(), 10)
        q = ArrayQueue(20)
        self.assertEqual(q.ReservedSize(), 20)
        q = ArrayQueue(5)
        self.assertEqual(q.ReservedSize(), 5)
        q.Enqueue(10).Enqueue(20)
        self.assertEqual(q.ReservedSize(), 5)
        q.Enqueue(30).Enqueue(40)
        self.assertEqual(q.ReservedSize(), 5)
        q.Enqueue(50)
        self.assertEqual(q.ReservedSize(), 10)
        q.Enqueue(60)
        self.assertEqual(q.ReservedSize(), 10)
        q.Enqueue(70).Enqueue(80).Enqueue(90).Enqueue(100)
        self.assertEqual(q.ReservedSize(), 20)
        q.Dequeue(); q.Dequeue(); q.Dequeue(); q.Dequeue();
        self.assertEqual(q.ReservedSize(), 20)
        q.Dequeue()
        self.assertEqual(q.ReservedSize(), 10)
        q.Dequeue()
        self.assertEqual(q.ReservedSize(), 10)
        q.Dequeue(); q.Dequeue(); q.Dequeue(); q.Dequeue();
        self.assertEqual(q.ReservedSize(), 10)
        self.assertEqual(q.Dequeue(), None)

class TestQueue(unittest.TestCase):
    def setUp(self):
        print "\nRun test for Queue"

    def test_queue(self):
        q = Queue()
        self.assertTrue(q.IsEmpty())
        self.assertEqual(q.Size(), 0)
        self.assertEqual(q.Dequeue(), None)
        q.Enqueue(10)
        self.assertTrue(not q.IsEmpty())
        self.assertEqual(q.Size(), 1)
        self.assertEqual(q.Dequeue(), 10)
        self.assertEqual(q.Size(), 0)
        self.assertEqual(q.Dequeue(), None)
        self.assertTrue(q.IsEmpty())
        q.Enqueue(10).Enqueue(20)
        self.assertTrue(not q.IsEmpty())
        self.assertEqual(q.Size(), 2)
        q.Enqueue(30).Enqueue(40)
        self.assertTrue(not q.IsEmpty())
        self.assertEqual(q.Size(), 4)
        self.assertEqual(q.Dequeue(), 10)
        self.assertEqual(q.Size(), 3)
        self.assertTrue(not q.IsEmpty())
        self.assertEqual(q.Dequeue(), 20)
        self.assertEqual(q.Size(), 2)
        self.assertTrue(not q.IsEmpty())
        self.assertEqual(q.Dequeue(), 30)
        self.assertEqual(q.Size(), 1)
        self.assertTrue(not q.IsEmpty())
        self.assertEqual(q.Dequeue(), 40)
        self.assertEqual(q.Size(), 0)
        self.assertTrue(q.IsEmpty())
        self.assertEqual(q.Dequeue(), None)

if __name__ == '__main__':
    unittest.main()

