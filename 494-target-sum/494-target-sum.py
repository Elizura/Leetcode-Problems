class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:        
        
        @cache
        def dfs(idx, amt):             
            if idx == len(nums):
                return amt == target            
            return dfs(idx + 1, amt + nums[idx]) + dfs(idx + 1, amt - nums[idx])                
        return dfs(0, 0)        
    
    
    # class Solution:
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:        
    #     # @cache
    #     def dfs(idx, amt): 
    #         nonlocal ans
    #         if idx == len(nums) and amt == target: ans += 1
    #         # if (idx, ) in dp: return dp[(idx, amt)]
    #         if idx >= len(nums): return
    #         dfs(idx + 1, amt + nums[idx])
    #         dfs(idx + 1, amt - nums[idx])
    #     # dp = {}
    #     ans = 0
    #     dfs(0, 0)
    #     return ans