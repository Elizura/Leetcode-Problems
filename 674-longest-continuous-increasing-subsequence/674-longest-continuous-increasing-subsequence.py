class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        temp = 1
        max_ = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                temp += 1
                max_ = max(max_, temp)
            else: 
                temp = 1
        return max_
            
#         O(n) time and O(1) space

#         O(n) time and O(n) space
        # ans = [1 for i in range(len(nums))]
        # for i in range(1, len(ans)):
        #     if nums[i] > nums[i - 1]:
        #         ans[i] = ans[i - 1] + 1
        # return max(ans)
