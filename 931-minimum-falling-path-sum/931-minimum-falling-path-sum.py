class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [i for i in matrix[0]]
        for row in range(1, len(matrix[0])):
            temp = [_ for _ in matrix[row]]
            for col in range(len(temp)):
                left = dp[col + 1] if col + 1 < len(dp) else inf
                right = dp[col - 1] if col - 1 >= 0 else inf
                temp[col] = min(dp[col], left, right) + temp[col]
            dp = temp
        return min(dp)
#         N = len(matrix)
#         @cache
#         def dfs(row, col):
#             if row >= N or col >= N: return inf
#             if col < 0: return inf
#             if row == N - 1: return matrix[row][col]
#             a = matrix[row][col] + dfs(row + 1, col)
#             b = matrix[row][col] + dfs(row + 1, col + 1)
#             c = matrix[row][col] + dfs(row + 1, col - 1)            
#             return min(a, b, c)
        
        
#         ans = inf
#         for i in range(N):
#             a = dfs(0, i)            
#             ans = min(ans, a)
#         return ans