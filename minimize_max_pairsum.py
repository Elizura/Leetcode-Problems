class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        ans=nums[l]+nums[r]
        while r>l:
            r-=1
            l+=1
            if nums[l]+nums[r]>ans:
                ans=nums[l]+nums[r]
        return ans
