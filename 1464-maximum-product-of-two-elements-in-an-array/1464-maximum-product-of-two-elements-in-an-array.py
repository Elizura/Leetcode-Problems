class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
        # #O(N) time and O(1) space
        # ans = 0
        # _max = nums[0] - 1
        # for j in range(1, len(nums)):
        #     ans = max(ans, _max*(nums[j] - 1))
        #     _max = max(_max, nums[j] - 1)
        # return ans