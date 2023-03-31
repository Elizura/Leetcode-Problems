class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        @cache
        def subsetsum(index, mod):
            if index >= len(nums): return -inf if mod else 0
            return max(nums[index] + subsetsum(index + 1, (mod + nums[index])%3),
            subsetsum(index + 1, mod))
        return subsetsum(0, 0)
#         n = len(nums)
#         dp = [[0]*(n) for _ in range(3)]
#         dp[nums[0]%3][0] = nums[0]
#         for i in range(1, len(nums)):
#             a = nums[i] + dp[0][i - 1]
#             b = nums[i] + dp[1][i - 1]
#             c = nums[i] + dp[2][i - 1]
#             for j in range(3):
#                 dp[j][i] = dp[j][i - 1]
#             dp[a%3][i] = max(dp[a%3][i], dp[a%3][i - 1], a)
#             dp[b%3][i] = max(dp[b%3][i], dp[b%3][i - 1], b)
#             dp[c%3][i] = max(dp[c%3][i], dp[c%3][i - 1], c)        
#         return dp[0][n - 1]
