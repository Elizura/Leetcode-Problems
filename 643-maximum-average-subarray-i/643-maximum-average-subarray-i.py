class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        ans = -inf
        pref = 0
        for right in range(len(nums)):
            pref += nums[right]            
            if right - left + 1 == k:                
                avg = pref / k                
                ans = max(ans, avg)                
                pref -= nums[left]
                left +=1            
        return ans