class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
    
        nums.sort()
        res = nums[-1] - nums[0]
        for i in range(len(nums) - 1):
            res = min(res, max(nums[-1] - k, nums[i] + k) - min(nums[0] + k, nums[i + 1] - k))
        return res
#         def dfs(idx, arr, sign):
#             if idx >= len(nums): return max(arr) - min(arr)
#             if (idx, sign) in memo: return memo[idx, sign]
#             arr1 = arr.copy()
#             arr2 = arr.copy()
#             arr1[idx] = arr1[idx] + k
#             arr2[idx] = arr2[idx] - k            
#             add = dfs(idx + 1, arr1, 1)
#             sub = dfs(idx + 1, arr2, 0)
#             memo[idx, sign] = min(add, sub)
#             return memo[idx, sign]
#         memo = {}
#         return dfs(0, nums, None)
            
            
#         nums.sort()
#         left, right = 0, len(nums) - 1
#         ans = inf
#         while right >= left:
#             ans = min(ans, abs((nums[left] + k) - (nums[right] - k)))
#             left += 1
#             right -= 1
#         return ans