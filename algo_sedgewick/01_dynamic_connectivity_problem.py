#!/usr/bin/env python2

import sys

# 1. the first way to solve dynamic connectivity problems
# An eager approach of union-find thought: quick-find
class QuickFindUF:
    # initialize with the number of objects
    def __init__(self, number):
        self.id = range(number)
        for i in range(number):
            self.id[i] = i

    def IsConnected(self, p, q):
        return self.id[p] == self.id[q]

    def Union(self, p, q):
        # change ids equal to p's to id of q
        old_id, new_id = self.id[p], self.id[q]
        for elem in self.id:
            elem = new_id if elem == old_id else elem

# 2. the lazy approach to the dynamic connectivity problem
# that is, the quick-union
class QuickUnionUF:
    def __init__(self, number):
        self.id = range(number)
        for i in range(number):
            self.id[i] = i

    def GetRoot(self, id):
        p = id
        while p != self.id[p]:
            p = self.id[p]
        return p

    def Union(self, p, q):
        proot = self.GetRoot(p)
        self.id[proot] = self.GetRoot(q)

    def IsConnected(self, p, q):
        return self.GetRoot(p) == self.GetRoot(q)

# 3. weight quick union
class QuickUnionWeighted:
    def __init__(self, number):
        self.id = range(number)
        self.sz = range(number)
        for i in range(number):
            self.id[i] = i
            self.sz[i] = 1

    def GetRoot(self, id):
        p = id
        while p != self.id[p]:
            p = self.id[p]
        return p

    def Union(self, p, q):
        proot = self.GetRoot(p)
        qroot = self.GetRoot(q)
        # set qroot = proot by default, unless #p_tree < #q_tree
        if self.sz[proot] < self.sz[qroot]:
            # attach p_tree to q_tree
            self.id[proot] = qroot
            self.sz[qroot] = self.sz[qroot] + self.sz[proot]
        else:
            # attach q_tree to p_tree
            self.id[qroot] = proot
            self.sz[proot] = self.sz[proot] + self.sz[qroot]
            
    def IsConnected(self, p, q):
        return self.GetRoot(p) == self.GetRoot(q)

# unit test
if __name__ == "__main__":
    if len(sys.argv) == 2:
        infile = open(sys.argv[1])
        initNum = int(infile.readline().strip())
        print "InitNum is %s" % initNum
        uf = QuickUnionWeighted(initNum)
        for line in infile:
            nums = [int(x) for x in line.strip().split()]
            if not uf.IsConnected(nums[0], nums[1]):
                uf.Union(nums[0], nums[1])
                print "Union %s and %s" % (nums[0], nums[1])
        infile.close()
    else:
        print "Usage: %s filename" % sys.argv[0]

        
    


