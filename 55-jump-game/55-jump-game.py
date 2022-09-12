class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        need = len(nums) - 1
        i = len(nums) - 2
        while i >= 0:
            if i + nums[i] >= need:
                need = i
            if need == 0: return True
            i -= 1
        return False