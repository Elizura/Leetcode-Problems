class unionFind(object):
    def __init__(self):
        self.rank = [0] * 1001
        self.parent = list(range(1001))
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
        # if self.parent[node] == node: return node
        # self.parent[node] = self.find(self.parent[node])
    def union(self, node1, node2) -> bool:
        pn1, pn2 = self.find(node1), self.find(node2)
        if pn1 == pn2: return False
        elif self.rank[pn1] > self.rank[pn2]:
            self.parent[pn2] = pn1
        elif self.rank[pn1] < self.rank[pn2]:
            self.parent[pn1] = pn2
        else:
            self.parent[pn2] = pn1
            self.rank[pn1] += 1
        return True
    
class Solution(object):
    def findRedundantConnection(self, edges):
        uf = unionFind()
        for node1, node2 in edges:
            if not uf.union(node1, node2): return [node1, node2]