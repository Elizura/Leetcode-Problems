class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        temp = 0
        for i in nums:
            temp += i
            ans = max(ans, temp)
            temp = max(temp, 0)
        return ans