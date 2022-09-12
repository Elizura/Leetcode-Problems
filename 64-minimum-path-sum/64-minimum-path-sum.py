class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # @cache
        def dfs(row, col):
            if (row, col) in dp: return dp[(row, col)]
            if row >= len(grid) or col >= len(grid[0]): return inf
            if row == len(grid) - 1 and col == len(grid[0]) - 1: return grid[-1][-1]
            down = dfs(row + 1, col) + grid[row][col]
            right = dfs(row, col + 1) + grid[row][col]
            dp[(row, col)] = min(down, right)
            return min(down, right)
        dp = {}
        return dfs(0, 0)