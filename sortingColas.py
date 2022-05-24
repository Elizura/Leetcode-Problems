class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=len(nums)
        count=[0]*3
        output=[0]*s
        for i in range(s):
            count[nums[i]]+=1
        for j in range(1,len(count)):
            count[j]= count[j]+count[j-1]
        i=s-1
        while i >=0:
            output[count[nums[i]]-1]=nums[i]
            count[nums[i]]-=1
            i-=1
        for i in range(0, s):
            nums[i] = output[i]
