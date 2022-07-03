class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reversel(num):
            l_=0
            r_=len(num)-1
            while r_>=l_:
                nums[l_],nums[r_]=nums[r_],nums[l_]
                r_-=1
                l_+=1
        def reverser(num):
            l_ = k
            r_ = len(nums) - 1
            while r_ >= l_:
                nums[l_], nums[r_] = nums[r_], nums[l_]
                r_ -= 1
                l_ += 1
        k=k%len(nums)
        l=0
        r=len(nums)-1
        while r>=l:
            nums[l],nums[r]=nums[r],nums[l]
            r-=1
            l+=1
        reversel(nums[:k])
        reverser(nums[k:])
        """
        Do not return anything, modify nums in-place instead.
        """
        
