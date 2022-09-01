class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = [1 for i in range(len(nums))]
        for i in range(1, len(ans)):
            if nums[i] > nums[i - 1]:
                ans[i] = ans[i - 1] + 1
        return max(ans)