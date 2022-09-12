class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        left = right = 0
        while right < len(nums) - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            ans += 1
        return ans
        
#         N = len(nums)
#         if N == 1: return 0
#         # @cache
#         def dfs(idx):
#             if dp[idx] != inf: return dp[idx]
#             if idx + nums[idx] >= N - 1: return 1
#             elif idx == N - 1: return 0
#             step = inf			
#             for i in range(1, nums[idx]+1):
#                 sub = 1 + dfs(idx + i)
#                 step = min(sub, step)
#             dp[idx] = step
#             return step
#         dp = [inf for i in range(len(nums))]
#         return dfs(0)
    
    
        # leng = len(nums)
        # if leng == 1: return 0
        # dp = [inf] * leng
        # dp[0] = 0
        # for i in range(1,leng):
        #     for j in range(i):
        #         if nums[j] + j >= i:
        #             dp[i] = min(dp[i], dp[j] + 1)
        # return dp[leng-1]
        
        # dp = [inf for i in range(len(nums))]
        # dp[0] = 0
        # for i in range(len(nums)):
        #     for j in range(1, nums[i] + 1):
        #         if i + j < len(dp):
        #             dp[i + j] = min(dp[i + j], dp[i] + 1)
        # return dp[-1]