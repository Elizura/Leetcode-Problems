class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(index, amount, memo = {}):
            if (amount, index) in memo: return memo[(amount, index)]
            if index >= len(nums): return amount
            rob = dfs(index + 2, amount + nums[index])
            skip = dfs(index + 1, amount)
            memo[(amount, index)] = max(rob, skip)
            return memo[(amount, index)]
        return dfs(0, 0)