class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 0
        _max = nums[0] - 1
        for j in range(1, len(nums)):
            ans = max(ans, _max*(nums[j] - 1))
            _max = max(_max, nums[j] - 1)
        return ans