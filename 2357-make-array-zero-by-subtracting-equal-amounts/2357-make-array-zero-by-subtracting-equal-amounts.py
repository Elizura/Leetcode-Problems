class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c,n=0,len(nums)
        def smallestNonZero():
            x=101
            for i in nums:
                if i==0:
                    continue
                if i<x:
                    x=i
            return x
        while sum(nums)!=0:
            c+=1
            x=smallestNonZero()
            for i in range(n):
                if nums[i]==0:
                    continue
                nums[i]-=x
        return c