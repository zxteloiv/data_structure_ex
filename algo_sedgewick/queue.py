#!/usr/bin/python2

# queue implementations are similar as those of stack except for the API name

from collections import deque

# 1. Implement a stack by using linked list first
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
    def __init__(self, stack_size=10):
        pass
        
    def Enqueue(self, val):
        return self
        pass

    def Dequeue(self):
        return None
        pass

    def IsEmpty(self):
        pass

    def Size(self):
        pass

    def ReservedSize(self):
        pass

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

