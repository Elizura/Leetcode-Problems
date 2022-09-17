class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        @cache
        def dfs(row, col):
            if row >= N or col >= N: return inf
            if col < 0: return inf
            if row == N - 1: return matrix[row][col]
            a = matrix[row][col] + dfs(row + 1, col)
            b = matrix[row][col] + dfs(row + 1, col + 1)
            c = matrix[row][col] + dfs(row + 1, col - 1)            
            return min(a, b, c)
        
        
        ans = inf
        for i in range(N):
            a = dfs(0, i)            
            ans = min(ans, a)
        return ans