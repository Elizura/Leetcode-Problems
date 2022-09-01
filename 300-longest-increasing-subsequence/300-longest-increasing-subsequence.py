class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # ans = [1 for _ in range(len(nums))]
        # for i in range(len(nums) - 1, -1, -1):
        #     for j in range(i, len(nums)):
        #         if nums[j] > nums[i]:
        #             ans[i] = max(ans[i], 1 + ans[j])
        # return max(ans)
        ans = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    ans[i] = max(ans[i], ans[j] + 1)
        return max(ans)