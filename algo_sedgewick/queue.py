#!/usr/bin/python2

# queue implementations are similar as those of stack except for the API name

from collections import deque

# 1. Implement a queue by using linked list first
class ListQueue:
    class Node:
        def __init__(self):
            self._val = None
            self._next = None
            self._prev = None

        def getval(self):
            return self._val
        def setval(self, val):
            self._val = val
        val = property(getval, setval)

        def getnext(self):
            return self._next
        def setnext(self, val):
            self._next = val
        next = property(getnext, setnext)

        def getprev(self):
            return self._next
        def setprev(self, val):
            self._prev = val
        prev = property(getnext, setnext)

    def __init__(self):
        self.head = self.Node()
        self.head.next = self.head
        self.head.prev = self.head
        self.size = 0

    def Enqueue(self, val):
        # actually enqueue is to insert after head
        newNode = self.Node()
        newNode.val = val
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next.prev = newNode
        self.head.next = newNode
        self.size = self.size + 1
        return self

    def Dequeue(self):
        # dequeue is to pop element at tail(head's prev)
        if (self.IsEmpty()):
            return None
        tail = self.head.prev
        val = tail.val
        tail.prev.next = tail.next
        tail.next.prev = tail.prev
        self.size = self.size - 1
        return val

    def IsEmpty(self):
        return self.size == 0

    def Size(self):
        return self.size

# 2. implement a queue using an array
class ArrayQueue:
    def __init__(self, queue_size=10):
        self.head = 0
        self.len = 0
        self.queue_size = queue_size
        self.queue = range(queue_size)
        
    def Enqueue(self, val):
        if self.head > 0:
            ins_pos = self.head - 1
        else:
            ins_pos = self.queue_size - 1
        self.queue[ins_pos] = val
        self.head = ins_pos
        self.len = self.len + 1
        
        # extend(double) the size of stack when it is full
        if self.len == self.queue_size:
            new_queue = range(2 * self.queue_size)
            # deep copy, pos starts from 0
            for pos in range(self.len):
                val_pos = (self.head + pos) % self.queue_size
                new_queue[pos] = self.queue[val_pos]
            self.queue = new_queue
            self.queue_size = self.queue_size * 2
        return self

    def Dequeue(self):
        if self.len == 0:
            return None
        rm_pos = (self.head + self.len - 1) % self.queue_size
        val = self.queue[rm_pos]
        self.len = self.len - 1

        # shrink(halve) the size of stack when it is 1/4 full
        # but at least 10 room is reserved
        if self.len <= self.queue_size / 4 and self.queue_size > 10:
            new_queue = range(self.queue_size / 2)
            # deep copy, pos starts from 0
            for pos in range(self.len):
                val_pos = (self.head + pos) % self.queue_size
                new_queue[pos] = self.queue[val_pos]
            self.queue = new_queue
            self.queue_size = self.queue_size / 2
        return val

    def IsEmpty(self):
        return self.len == 0

    def Size(self):
        return self.len

    def ReservedSize(self):
        return self.queue_size

# 3. implement a queue using a library provided by python
class Queue:
    def __init__(self):
        self.queue = deque([])

    def Enqueue(self, val):
        self.queue.append(val)
        return self

    def Dequeue(self):
        return self.queue.popleft() if self.Size() > 0 else None

    def IsEmpty(self):
        return 0 == len(self.queue)

    def Size(self):
        return len(self.queue)

