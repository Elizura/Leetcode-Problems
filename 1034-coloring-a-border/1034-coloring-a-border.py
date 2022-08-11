class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:  
        seen = set()
        colour = grid[row][col]
        def dfs(grid, row, col, color):
            if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] != colour or (row, col) in seen:
                return 
            elif row == 0 or col == 0 or row == len(grid) - 1 or col == len(grid[0]) - 1 or grid[row + 1][col] != colour or  grid[row - 1][col] != colour or  grid[row][col + 1] != colour or  grid[row][col - 1] != colour:                                
                seen.add((row, col))                
                dfs(grid, row + 1, col, color)
                dfs(grid, row - 1, col, color)
                dfs(grid, row, col + 1, color)
                dfs(grid, row, col - 1, color)
                grid[row][col] = color
            else:
                seen.add((row, col))
                dfs(grid, row + 1, col, color)
                dfs(grid, row - 1, col, color)
                dfs(grid, row, col + 1, color)
                dfs(grid, row, col - 1, color)
                
            return grid        
        return dfs(grid, row, col, color)