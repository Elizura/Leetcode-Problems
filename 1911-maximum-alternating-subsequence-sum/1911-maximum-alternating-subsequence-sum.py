class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        odd, even = 0, 0
        for i in range(0, len(nums)):
            odd = max(even + nums[i], odd)
            even = max(odd - nums[i], even)
        return odd
#         def dfs(index, odd):
#             if index >= len(nums):
#                 return 0
            
#             if odd:
#                 return max(dfs(index + 1, not odd) + nums[index], dfs(index + 1, odd))
#             else:
#                 return max(dfs(index + 1, not odd) - nums[index], dfs(index + 1, odd))
            
#         return dfs(0, 1)
#         def dfs(index, even):
#             if index >= len(nums): return 0              
#             if even:
#                 return max(nums[index] + dfs(index + 1, not even), dfs(index + 1, even))
#             else:
#                 return max(-nums[index] + dfs(index + 1, not even), dfs(index + 1, even))
            
#         return dfs(0, 1)