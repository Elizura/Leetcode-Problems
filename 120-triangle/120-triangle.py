class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dfs(idx, row):
            if row >= len(triangle): return 0
            if idx >= len(triangle[row]): return 0
            a = triangle[row][idx] + dfs(idx, row + 1)
            b = triangle[row][idx] + dfs(idx + 1, row + 1)
            return min(a, b)
        return dfs(0, 0)
#         idx = 0
#         ans = triangle[0][0]
#         for row in range(1, len(triangle)):
#             ans += min(triangle[row][idx], triangle[row][idx + 1])
#             if triangle[row][idx] > triangle[row][idx + 1]: idx += 1
#         return ans
                