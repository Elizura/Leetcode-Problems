class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        @lru_cache(None)
        def dfs(i):
            if i >= n:
                return 0
            return max(dfs(i+1),questions[i][0] + dfs(i+questions[i][1]+1))
        return dfs(0)
#         a, b = 0, 0
#         for i in questions:
#             a, b = b, max(i[0])
        
#         def dfs(idx, pts, memo = {}):
#             if (idx, pts) in memo: return memo[(idx, pts)]
#             if idx >= len(questions): return pts
            
#             solve = dfs(idx + questions[idx][-1] + 1, pts + questions[idx][0])
#             dont = dfs(idx + 1, pts)
            
#             memo[(idx, pts)] = max(solve, dont)
#             return memo[(idx, pts)]
        
#         return dfs(0, 0)