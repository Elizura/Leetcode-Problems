class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        def calcsum(row, col, n, m):            
            tot = 0
            for i in range(max(0, row - k), min(n, row + k + 1)):
                for j in range(max(0, col - k), min(m, col + k + 1)):
                    tot += mat[i][j]
            return tot
        ans = [[0]*m for i in range(n)]
        for r in range(n):
            for c in range(m):
                d = calcsum(r, c, n, m)                
                ans[r][c] = d
        return ans