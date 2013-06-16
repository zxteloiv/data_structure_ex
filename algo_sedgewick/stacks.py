#!/usr/bin/python2

# 1. Implement a stack by using linked list first
class ListStack:
    class Node:
        def __init__(self):
            self._val = None
            self._next = None

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

    def __init__(self):
        self.head = self.Node()
        self.size = 0

    def Push(self, val):
        newNode = self.Node()
        newNode.val = val
        newNode.next = self.head.next
        self.head.next = newNode
        self.size = self.size + 1
        return self

    def Pop(self):
        if (self.IsEmpty()):
            return None
        val = self.head.next.val
        self.head = self.head.next
        self.size = self.size - 1
        return val

    def IsEmpty(self):
        return self.head.next == None

    def Size(self):
        return self.size

# 2. implement a stack using an array
class ArrayStack:
    def __init__(self, stack_size=10):
        self.stack = range(stack_size)
        self.usage = 0
        self.stack_size = stack_size
        
    def Push(self, val):
        # list index starts from 0
        self.stack[self.usage] = val
        self.usage = self.usage + 1

        # extend(double) the size of stack when it is full
        if self.usage == self.stack_size:
            new_stack = range(2 * self.stack_size)
            new_stack[0:self.usage] = self.stack
            self.stack = new_stack
            self.stack_size = self.stack_size * 2
        return self

    def Pop(self):
        if self.usage == 0:
            return None
        val = self.stack[self.usage - 1]
        self.usage = self.usage - 1

        # shrink(halve) the size of stack when it is 1/4 full
        # but at least 10 room is reserved
        if self.usage <= self.stack_size / 4 and self.stack_size > 10:
            new_stack = range(self.stack_size / 2)
            new_stack[0:self.usage] = self.stack[0:self.usage]
            self.stack = new_stack
            self.stack_size = self.stack_size / 2
        return val

    def IsEmpty(self):
        return self.usage == 0

    def Size(self):
        return self.usage

    def ReservedSize(self):
        return self.stack_size

# 3. implement a stack using python list in a easier way
class Stack:
    def __init__(self):
        self.stack = []

    def Push(self, val):
        self.stack.append(val)
        return self

    def Pop(self):
        return self.stack.pop() if self.Size() > 0 else None

    def IsEmpty(self):
        return 0 == len(self.stack)

    def Size(self):
        return len(self.stack)
