    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        size=len(nums)
        output=[0]*size
        for i in range(size):
            for j in range(size):
                if nums[i]>nums[j]:
                    output[i]+=1
        return output
