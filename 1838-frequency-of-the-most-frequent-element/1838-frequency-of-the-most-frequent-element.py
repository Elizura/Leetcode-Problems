class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        largest_freq=0
        l=r=0
        total=0
        for i in range(len(nums)):
            total+=nums[r]
            
            while nums[r]*(r-l+1)>k+total:
                #subtract the number from the total
                #shrink the size by moving the left pointer forwards
                total-=nums[l]
                l+=1
            largest_freq=max(largest_freq,r-l+1)
            r+=1
        return largest_freq
                
        