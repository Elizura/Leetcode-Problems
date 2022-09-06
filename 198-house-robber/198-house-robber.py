class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        # if len(nums)==1:
        #     return nums[0]
        # dp = {}
        # dp[0] = nums[0]
        # dp[1] = max(nums[0:2]) 
        # for i in range(2,len(nums)):
        #     dp[i] = max(dp[i-1],nums[i]+dp[i-2])          
        # return(max(dp.values()))
        # take, nottake = 0 , 0 
        # for index in range(len(nums)):
        #     take = nottake + nums[index]
        #     nottake = max(take, nottake)
        # return max(take, nottake)
    
#         _min = 0
#         _max = 0
#         for i in range(len(nums)):
#             _max = max(_min + nums[i], _max)
#             _min = min(_min + nums[i], _min)
#         return max(_max, _min)
        # def dfs(index, amount, memo = {}):
        #     if (amount, index) in memo: return memo[(amount, index)]
        #     if index >= len(nums): return amount
        #     rob = dfs(index + 2, amount + nums[index])
        #     skip = dfs(index + 1, amount)
        #     memo[(amount, index)] = max(rob, skip)
        #     return memo[(amount, index)]
        # return dfs(0, 0)