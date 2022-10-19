class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        pref = 0
        left = 0
        max_freq = 0
        for right, num in enumerate(nums):            
            pref += num
            while pref + k < num * (right - left + 1):                
                pref -= nums[left]
                left += 1
            max_freq = max(max_freq, right - left + 1)
        return max_freq