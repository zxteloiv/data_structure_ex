class BST:
    class Node:
        def __init__(self, key=None, val=None):
            self._key = key
            self._val = val
            self._left = None
            self._right = None

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

    def __init__(self):
        self.root = None
        self.size = 0

    def Put(self, key, val):
        if not self.root:
            self.root = BST.Node(key, val)
            self.size += 1
        else:
            self._insert(self.root, key, val)

    def _insert(self, node, key, val):
        if key == node.key: node.val = val
        elif key < node.key:
            if not node.left:
                node.left = BST.Node(key, val)
                self.size += 1
            else:
                self._insert(self.node.left, key, val)
        else:
            if not node.right:
                node.right = BST.Node(key, val)
                self.size += 1
            else:
                self._insert(self.node.right, key, val)

    def Get(self, key): return self._find(self.root, key)

    def _find(self, node, key):
        if not node: return None
        if key == node.key: return node.val
        elif key < node.key: return self._find(node.left, key)
        else: return self._find(node.right, key)

    def Size(self): return self.size

    def Delete(self, key):
        pass
