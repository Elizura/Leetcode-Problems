class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if i%2==0:
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
            if i%2:
                if nums[i+1]>nums[i]:
                    nums[i+1],nums[i]=nums[i],nums[i+1]
                    
        return nums