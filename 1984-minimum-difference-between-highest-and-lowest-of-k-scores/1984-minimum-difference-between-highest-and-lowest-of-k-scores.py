class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = inf
        nums.sort()
        left = 0
        for right in range(len(nums)):
            lowest = nums[left]
            highest = nums[right]
            if right - left + 1 == k:
                ans = min(ans, highest - lowest)
                left += 1
        return ans
                
            
        