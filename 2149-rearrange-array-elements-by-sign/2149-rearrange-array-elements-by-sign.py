class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0 for i in range(len(nums))]
        even = 0
        odd = 1
        for i in range(len(nums)):
            if nums[i] > 0:
                ans[even] = nums[i]
                even += 2
            else:
                ans[odd] = nums[i]
                odd += 2
        return ans
            
        #O(N^2) time and O(N) space TLE
        # need = 1
        # arr = []
        # j = 0
        # seen = set()
        # while len(arr) != len(nums) and j < len(nums):
        #     if need and nums[j] > 0 and j not in seen:
        #         arr.append(nums[j])
        #         seen.add(j)
        #         need = not need
        #         j = 0
        #     elif not need and nums[j] < 0 and j not in seen:
        #         arr.append(nums[j])
        #         seen.add(j)
        #         need = not need
        #         j = 0
        #     else:                
        #         j += 1
        # return arr