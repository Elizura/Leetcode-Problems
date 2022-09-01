class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # ans = -inf
        # temp = 0
        # for i in nums:
        #     temp += i
        #     ans = max(ans, temp)
        #     temp = max(temp, 0)
        # return ans
#         O(N) time and O(N) space
        # ans = [nums[_] for _ in range(len(nums))]        
        # for i in range(1, len(nums)):
        #     ans[i] = max(nums[i], ans[i - 1] + nums[i])
        # return max(ans)
        ans = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
            ans = max(ans, nums[i])
        return ans