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

    def Push(self, val):
        newNode = self.Node()
        newNode.val = val
        newNode.next = self.head.next
        self.head.next = newNode
        return self

    def Pop(self):
        if (self.IsEmpty()):
            return None
        val = self.head.next.val
        self.head = self.head.next
        return val

    def IsEmpty(self):
        return self.head.next == None

