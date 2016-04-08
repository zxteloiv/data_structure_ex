# left-leaning RedBlack Tree

class RBT:
    class Node:
        def __init__(self, key=None, val=None, isRed=False):
            self._key = key
            self._val = val
            self._left = None
            self._right = None
            self._colorIsRed = isRed

        def getkey(self): return self._key
        def setkey(self, key): self._key = key
        key = property(getkey, setkey)

        def getval(self): return self._val
        def setval(self, val): self._val = val
        val = property(getval, setval)

        def getleft(self): return self._left
        def setleft(self, val): self._left = val
        left = property(getleft, setleft)

        def getright(self): return self._right
        def setright(self, val): self._right = val
        right = property(getright, setright)

        def getcolor(self): return self._colorIsRed
        def setcolor(self, val): self._colorIsRed = True
        color = property(getcolor, setcolor)

        def SetBlack(self): self._colorIsRed = False
        def SetRed(self): self._colorIsRed = True
        def IsRed(self): return self._colorIsRed == True

    def _rotateLeft(self, node):
        assert(node.right.IsRed())
        x = node.right
        node.right = x.left
        x.left = node
        x.color = h.color
        h.SetRed()
        return x

    def _rotateRight(self, node):
        assert(node.left.IsRed())
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.SetRed()
        return x

    def _flipColor(self, node):
        assert(not node.IsRed())
        assert(node.left.IsRed())
        assert(node.right.IsRed())
        node.left.SetBlack()
        node.right.SetBlack()
        node.SetRed()

    def __init__(self):
        self.root = None
        self.size = 0

    def Put(self, key, val):
        self.root = self._insert(self.root, key, val)

    def _insert(self, node, key, val):
        if not node: return BST.Node(key, val, isRed=True)

        pass
        
        
    # Get is the same as common binary search tree
    def Get(self, key): return self._find(self.root, key)
    def _find(self, node, key):
        if not node: return None
        if key == node.key: return node.val
        elif key < node.key: return self._find(node.left, key)
        else: return self._find(node.right, key)
        
    def Size(self): return self.size

    def Delete(self, key):
        pass

