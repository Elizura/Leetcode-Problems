class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # @cache
        def dfs(row, col):
            if (row, col) in memo: return memo[row, col]
            if 0 > row or row >= len(obstacleGrid) or 0 > col or col >= len(obstacleGrid[0]): return 0
            if row == len(obstacleGrid) - 1 and col == len(obstacleGrid[0]) - 1: return 1
            if obstacleGrid[row][col] == 1: return 0
            memo[row, col] = dfs(row + 1, col) + dfs(row, col + 1)
            return memo[row, col]
        if obstacleGrid[-1][-1] == 1: return 0
        memo = {}
        return dfs(0, 0)