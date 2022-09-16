class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # dp[1][1] = 1
        # for i in range(m + 1):
        #     for j in range(n + 1):                
        #         if i + 1 <= m:
        #             dp[i + 1][j] += dp[i][j]
        #         if j + 1 <= n:
        #             dp[i][j + 1] += dp[i][j]        
        # return dp[-1][-1]
#         def dfss(row, col, memo = {}):
#             if (row, col) in memo: return memo[(row, col)]            
#             if row >= m or col >= n: return 0
#             if row == m - 1 and col == n - 1: return 1
#             r = dfss(row, col + 1)
#             l = dfss(row + 1, col)
#             memo[(row, col)] = l + r            
#             return l + r
            
        def dfs(row, col, memo = {}):
            key = (row, col)
            if key in memo: return memo[key]
            if row == 0 or col == 0: return 0
            if row == 1 and col == 1: return 1
            memo[key] = dfs(row - 1, col) + dfs(row, col - 1)
            return memo[key]
        return dfs(m, n)
        