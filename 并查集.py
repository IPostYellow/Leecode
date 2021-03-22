class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.find(p)
        return self.parent[p]

    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot != qroot:
            self.parent[proot] = qroot
            self.count -= 1


class UnionFinds:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.find(p)
        return self.parent[p]

    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot != qroot:
            self.parent[proot] = qroot
            self.count -= 1

    def IsConnect(self, p, q):
        return self.find(q) == self.find(p)


class Union_Find:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.count=n
    def find(self,p):
        if p!=self.parent[p]:
            self.parent[p]=self.find(p)
        return self.parent[p]
    def union(self,p,q):
        proot=self.find(p)
        qroot=self.find(q)
        if proot!=qroot:
            self.parent[proot]=qroot
            self.count-=1