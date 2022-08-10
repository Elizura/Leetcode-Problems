class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        seen = set()
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
                return 1
            if  (row, col) in seen:
                return 0          
            else:
                seen.add((row, col))
                return dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1)
        a = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    a += dfs(i, j)
        return a