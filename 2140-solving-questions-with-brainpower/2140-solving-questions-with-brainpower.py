class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        tab = [i[0] for i in questions]
        for i in range(len(questions) - 2, -1, -1):
            if i + questions[i][-1] + 1 < len(tab):
                tab[i] = max(questions[i][0] + tab[i + questions[i][-1] + 1], tab[i + 1])
            else:
                tab[i] = max(tab[i], tab[i + 1])
        return max(tab)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n = len(questions)
#         dp = [0 for _ in range(n)]
        
#         for i in range(n-1, -1, -1):
#             idx = i + questions[i][1] + 1
#             if idx < n:
#                 dp[i] = dp[idx] + questions[i][0]
#             else:
#                 dp[i] = questions[i][0]
            
#             if i < n-1:
#                 dp[i] = max(dp[i], dp[i+1])
        
#         return dp[0]
        # n = len(questions)
        # # @lru_cache(None)
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     return max(dfs(i+1),questions[i][0] + dfs(i+questions[i][1]+1))
        # return dfs(0)
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