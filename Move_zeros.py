def moveZeroes(self, nums: List[int]) -> None:
        l=0
        r=1
        i=0
        while l<len(nums) and r<len(nums) and nums[l]!=0:
            l+=1
            r+=1
        while i<len(nums) and l<len(nums) and r<len(nums):
            if nums[r]!=0:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
            r+=1
            i+=1
        """
        Do not return anything, modify nums in-place instead.
        """
        
