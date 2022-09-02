class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maks = [i for i in nums]
        mean = [i for i in nums]
        maks[0] = mean[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                maks[i] = max(nums[i]*maks[i - 1], nums[i])
                mean[i] = min(nums[i]*mean[i - 1], nums[i])
            else:
                maks[i] = max(nums[i]*mean[i - 1], nums[i])
                mean[i] = min(nums[i]*maks[i - 1], nums[i])       
        return max(maks)
        # max_ = -inf
        # j = 0
        # while j < len(nums):
        #     a = 1
        #     for i in range(j, len(nums)):            
        #         a = a * nums[i]                
        #         max_ = max(max_, a)                            
        #     j += 1            
        # return max_           