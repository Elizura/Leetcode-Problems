class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for num in nums:
            if num - 1 not in nums_set:
                longest = 1
                while num + 1 in nums_set:
                    longest += 1
                    num += 1
                ans = max(ans, longest)
        return ans
#         if not nums: return 0
#         seen = set()
#         dic = {v:i for i, v in enumerate(nums)}               
#         def dfs(idx):
#             if nums[idx] in seen: return 0
#             if idx >= len(nums): return 0
#             fro = 0
#             back = 0
#             if nums[idx] - 1 in dic:
#                 seen.add(nums[idx])
#                 back = 1 + dfs(dic[nums[idx] - 1])
#             if nums[idx] + 1 in dic:
#                 seen.add(nums[idx])
#                 fro = 1 + dfs(dic[nums[idx] + 1])
#             return fro + back
        
        
#         ans = 0        
#         for i in range(len(nums)):
#             ans = max(ans, dfs(i))
#         return ans + 1
            