class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        N = len(nums)
        dp = [0 for i in range(N)]
        dp[-1] = nums[-1]
        for start in range(N - 2, -1, -1):
            temp = [0 for i in range(N)]
            for end in range(start, N):
                if start == end:
                    temp[end] = nums[start]
                else:
                    temp[end] = max(-dp[end] + nums[start], -temp[end - 1] + nums[end])
            dp = temp
        print(dp)
        return dp[-1] >= 0
    
    
        # N = len(nums)
        # dp = [[0 for i in range(N)] for i in range(N)]
        # for start in range(N - 1, -1, -1):
        #     for end in range(start, N):
        #         if start == end:
        #             dp[start][end] = nums[start]
        #         else:
        #             dp[start][end] = max(nums[start] - dp[start + 1][end], nums[end] - dp[start][end - 1])
        # return dp[0][-1] >= 0
        
        # N = len(nums)
        # @cache
        # def dfs(l, r, turn):
        #     if l == r: return turn * nums[r]                        
        #     a = turn * nums[l] + dfs(l + 1, r, -turn)
        #     b = turn * nums[r] + dfs(l, r - 1, -turn)
        #     return turn * max(turn * a, turn * b)
        # return dfs(0, N - 1, 1) >= 0
        
        # N = len(nums)
        # # @cache
        # def dfs(l, r):
        #     if (l, r) in memo: return memo[l, r]
        #     N = len(nums)
        #     if l == r: return nums[l]            
        #     turn = N - (r - l + 1)
        #     if not turn % 2:
        #         memo[l, r] = max(nums[l] + dfs(l + 1, r), nums[r] + dfs(l, r - 1))
        #         return memo[l, r]
        #     else:   
        #         memo[l, r] = min(-nums[l] + dfs(l + 1, r), -nums[r] + dfs(l, r - 1))   
        #         return memo[l, r]
        # memo = {}
        # return dfs(0, N - 1) >= 0
        
        
        

        