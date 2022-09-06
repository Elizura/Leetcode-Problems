class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = 0
        dic = {0: 1}
        ans = 0
        for i in nums:
            pref += i
            if pref - k in dic:
                ans += dic[pref - k]                
            if pref in dic:
                dic[pref] += 1
            if pref not in dic: dic[pref] = 1
        return ans
        
        
        # def dfs(index, total):            
#             if index >= len(nums): return 0
#             total += nums[index]
#             if k < 0:
#                 if total < k: return 0
#             if k > 0:
#                 if total > k: return 0
#             if total == k: return 1            \U0001f60a\U0001f60a\U0001f60a\U0001f60a\U0001f60a\U0001f60a\U0001f60a
                        
#             return dfs(index + 1, total)
        
#         ans = 0
#         for i in range(len(nums)):
#             a = dfs(i, 0)
#             ans += a
            
#         return ans
        
            
        