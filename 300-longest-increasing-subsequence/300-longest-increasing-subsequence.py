class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [1 for _ in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    ans[i] = max(ans[i], 1 + ans[j])
        return max(ans)