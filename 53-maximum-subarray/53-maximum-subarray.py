class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        temp = nums[0]
        for i in range(1, len(nums)):
            temp = max(nums[i], nums[i] + temp)
            ans = max(temp, ans)
        return ans