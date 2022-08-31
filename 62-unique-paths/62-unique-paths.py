class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfss(row, col, memo = {}):
            if (row, col) in memo: return memo[(row, col)]
            # if (col, row) in memo: return memo[(col, row)]
            if row >= m or col >= n: return 0
            if row == m - 1 and col == n - 1: return 1
            r = dfss(row, col + 1)
            l = dfss(row + 1, col)
            memo[(row, col)] = l + r
            # memo[(col, row)] = l + r
            return l + r
            
        # def dfs(row, col):            
        #     if row == 0 or col == 0: return 0
        #     if row == 1 and col == 1: return 1
        #     return dfs(row - 1, col) + dfs(row, col - 1)
        return dfss(0, 0)
        