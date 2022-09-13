class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        r = 0        
        content = 0
        for i in range(len(s)):
            if r >= len(g):
                break
            if s[i] >= g[r]:
                content += 1                
                r += 1
        return content
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # ans = 0
        # l = 0
        # r = 0
        # g.sort()
        # s.sort()
        # while l < len(g) and r < len(s):
        #     if s[r] >= g[l]:
        #         ans += 1
        #         l += 1
        #         r += 1
        #     else:
        #         r += 1
        # return ans
        
        
        # N = min(len(s), len(g))
        # g.sort()
        # s.sort()
        # ans = 0
        # idx = 0
        # for i in range(N):
        #     for j in range(idx, N):
        #         if s[j] >= g[i]:
        #             ans += 1
        #             idx = j
        #             break
        # return ans
        