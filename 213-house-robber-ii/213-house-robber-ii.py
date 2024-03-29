class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.rob_em(nums[1:]), self.rob_em(nums[:-1]))

    def rob_em(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            rob1, rob2 = rob2, max(rob2, rob1 + n)          
        return rob2
        