class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        a = lambda row: 0 <= row < m
        b = lambda col: 0 <= col < n
        land_cells = 0        
        def dfs(row, col):
            if not a(row) or not b(col):
                return
            if grid[row][col] == 0:
                return 
            grid[row][col] = 0            
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        for col in range(len(grid[0])):
            if grid[0][col] == 1:
                dfs(0, col)
            if grid[len(grid) - 1][col] == 1:
                dfs(len(grid) - 1, col)
        for row in range(len(grid)):
            if grid[row][0] == 1:
                dfs(row, 0)
            if grid[row][len(grid[0]) - 1] == 1:
                dfs(row, len(grid[0]) - 1)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    land_cells += 1
        return land_cells
        