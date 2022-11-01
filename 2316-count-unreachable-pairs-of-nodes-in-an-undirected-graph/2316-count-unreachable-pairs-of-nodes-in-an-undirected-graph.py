class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, node1, node2):
        par1 = self.find(node1)
        par2 = self.find(node2)
        if par1 == par2: return False
        if self.size[par2] > self.size[par1]:
            par1, par2 = par2, par1
        self.size[par1] += self.size[par2]
        self.parent[par2] = par1
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:        
        uf = UnionFind(n)    
        for node1, node2 in edges:                                            
            uf.union(node1, node2)        
        for i in range(n):
            uf.find(i)
        count = Counter(uf.parent)                
        count = [i for i in count.values()]                 
        ans = 0                
        
        p1 = (sum(count))**2
        p2 = sum([x*x for x in count])

        ans = (p1- p2) // 2

        return ans
    
    