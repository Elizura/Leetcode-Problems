class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(index, nums, memo = {}):
            if index in memo: return memo[index]
            if index >= len(nums): return 0
            maks = 1
            for i in range(index, len(nums)):
                if nums[i] > nums[index]:
                    maks = max(maks, dfs(i, nums) + 1)
            memo[index] = maks
            return memo[index]
        makss = 1
        for i in range(len(nums)):
            makss = max(makss, dfs(i, nums))
        return makss
        # ans = [1 for _ in range(len(nums))]
        # for i in range(len(nums) - 1, -1, -1):
        #     for j in range(i, len(nums)):
        #         if nums[j] > nums[i]:
        #             ans[i] = max(ans[i], 1 + ans[j])
        # return max(ans)
        # ans = [1 for _ in range(len(nums))]
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             ans[i] = max(ans[i], ans[j] + 1)
        # return max(ans)