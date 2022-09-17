class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[i[j] for j in range(len(i))] for i in grid]        
        for row in range(len(dp)):
            for col in range(len(dp[0])):               
                if row == 0 and col == 0: continue
                if row == 0:                    
                    dp[row][col] += dp[row][col - 1]                                        
                if col == 0:                                        
                    dp[row][col] += dp[row - 1][col]                    
                elif row != 0 and col != 0:                    
                    dp[row][col] += min(dp[row][col - 1], dp[row - 1][col])                
        return dp[-1][-1]
        
        
        
        
        # row, col = len(grid), len(grid[0])
        # dp = [[0] * col for i in range(row)]        
        # dp[0][0] = grid[0][0]
        # for j in range(1, col):
        #     dp[0][j] = dp[0][j-1] + grid[0][j]
        # for i in range(1, row):   
        #     dp[i][0] = dp[i-1][0]+ grid[i][0]
        # for i in range(1,row):
        #     for j in range(1, col):               
        #             dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # return dp[-1][-1]
        # # @cache
        # def dfs(row, col):
        #     if (row, col) in dp: return dp[(row, col)]
        #     if row >= len(grid) or col >= len(grid[0]): return inf
        #     if row == len(grid) - 1 and col == len(grid[0]) - 1: return grid[-1][-1]
        #     down = dfs(row + 1, col) + grid[row][col]
        #     right = dfs(row, col + 1) + grid[row][col]
        #     dp[(row, col)] = min(down, right)
        #     return min(down, right)
        # dp = {}
        # return dfs(0, 0)