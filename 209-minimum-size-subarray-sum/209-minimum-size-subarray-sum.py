class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         pref = 0
#         left = 0
#         ans = inf
#         for right in range(2*len(nums)):
#             if right < len(nums):
#                 pref += nums[right]                         
#             if pref > target:
#                 pref -= nums[left]
#                 left += 1
#             if pref == target:                
#                 ans = min(ans, right - left + 1)
            
#         return ans
        ans = inf
        sun = 0
        l, r = 0, 0
        while r <= len(nums) and r >= l:            
            if sun < target:
                if r == len(nums): break
                sun += nums[r]
                r += 1
            else:
                ans = min(ans, r - l)
                sun -= nums[l]                
                l += 1
                
        return 0 if ans is inf else ans

