class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n
    def find(self, k):
        if self.parent[k] != k:
            self.parent[k] = self.find(self.parent[k])
        return self.parent[k]
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x == y: return False        
        if self.size[y] > self.size[x]:
            x, y = y, x
        self.size[x] += self.size[y]
        self.parent[y] = x
        return True
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dic = {}
        idx = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dic[i, j] = idx
                    idx += 1
        uf = UnionFind(idx)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if r > 0 and grid[r - 1][c] == 1:
                        uf.union(dic[r, c], dic[r - 1, c])                        
                    if c > 0 and grid[r][c - 1] == 1:
                        uf.union(dic[r, c], dic[r, c - 1])                          
        for i in range(idx):
            uf.find(i)
        count = collections.Counter(uf.parent)                
        count = [i for i in count.values()]        
        return 0 if len(count) == 0 else max(count)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        