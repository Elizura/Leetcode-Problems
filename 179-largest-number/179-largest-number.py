class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if int(nums[j+1]+nums[j])>int(nums[j]+nums[j+1]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return  '0' if int (''.join(nums))==0 else ''.join(nums)
        