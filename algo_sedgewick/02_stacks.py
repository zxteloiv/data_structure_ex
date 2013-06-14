#!/usr/bin/python2

import sys

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
        self.head = Node()

    def Push(self, val):
        pass

    def Pop(self):
        pass

    def IsEmpty(self):
        return self.head.next == None
        
if __name__ == "__main__":
    if False:
        pass
    else:
        print "Usage: %s " % sys.argv[0]
