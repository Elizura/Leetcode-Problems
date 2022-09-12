class Solution:
    def jump(self, nums: List[int]) -> int:
        leng = len(nums)
        if leng == 1: return 0
        @cache
        def dfs(loc):
            if loc + nums[loc] >= leng-1: return 1
            elif loc == leng-1: return 0
            step = inf			
            for i in range(1, nums[loc]+1):
                sub = 1 + dfs(loc+i)
                step = min(sub, step)
            return step
        return dfs(0)
    
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