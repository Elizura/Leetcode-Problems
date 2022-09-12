class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        pref = 0
        for i in nums:
            if i == 1:
                pref += 1
                ans = max(ans, pref)
            else:
                pref = 0
        return ans