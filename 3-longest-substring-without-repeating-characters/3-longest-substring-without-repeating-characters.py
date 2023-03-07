class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:      
        letters = {}
        left = 0
        ans = -inf
        N = len(s)        
        for right in range(N):                        
            while s[right] in letters:
                del letters[s[left]]
                left += 1                                            
            letters[s[right]] = 1
            ans = max(ans, right - left + 1)
        return max(ans, N - left)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         t = ''
#         N = len(s)
#         l, r, ans = 0, 0, 0
#         while r < N:
#             if s[r] not in t:
#                 t = s[l : r + 1]
#                 ans = max(ans, r - l + 1)
#             else:
#                 ans = max(ans, r - l + 1)
#                 l += 1            
#             r += 1                    
            
#         return ans