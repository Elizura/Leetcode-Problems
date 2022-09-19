class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # N = len(nums)
        # @cache
        # def dfs(l, r, turn):
        #     if l == r: return turn * nums[r]                        
        #     a = turn * nums[l] + dfs(l + 1, r, -turn)
        #     b = turn * nums[r] + dfs(l, r - 1, -turn)
        #     return turn * max(turn * a, turn * b)
        # return dfs(0, N - 1, 1) >= 0
        
        N = len(nums)
        # @cache
        def dfs(l, r):
            if (l, r) in memo: return memo[l, r]
            N = len(nums)
            if l == r: return nums[l]            
            turn = N - (r - l + 1)
            if not turn % 2:
                memo[l, r] = max(nums[l] + dfs(l + 1, r), nums[r] + dfs(l, r - 1))
                return memo[l, r]
            else:   
                memo[l, r] = min(-nums[l] + dfs(l + 1, r), -nums[r] + dfs(l, r - 1))   
                return memo[l, r]
        memo = {}
        return dfs(0, N - 1) >= 0
        

        