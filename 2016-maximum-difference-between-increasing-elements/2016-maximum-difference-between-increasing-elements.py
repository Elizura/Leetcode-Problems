class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        _min = nums[0]        
        ans = -inf
        for i in range(1, len(nums)):
            _min = min(_min, nums[i])
            dif = nums[i] - _min
            ans = max(ans, dif)
        return -1 if ans == 0 else ans
        