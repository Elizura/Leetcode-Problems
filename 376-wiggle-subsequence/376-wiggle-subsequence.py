class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        length = 1
        up = None
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and up != True:
                length += 1
                up = True
            if nums[i] < nums[i - 1] and up != False:
                length += 1
                up = False
        return length
        
        # #O(n) TC and O(N) SC
        # ans = 2
        # N = len(nums)
        # dp = [nums[i] - nums[i - 1] for i in range(1, N) if nums[i] - nums[i - 1] != 0]
        # if not dp: return 1
        # for i in range(1, len(dp)):
        #     if dp[i - 1] > 0 and dp[i] < 0 or dp[i - 1] < 0 and dp[i] > 0:
        #         ans += 1
        # return ans
    
        #O(N^2) time and O(1) space
        # ans = 1
        # pt = 1
        # N = len(nums)
        # if N == 1: return 1
        # for i in range(N):            
        #     if i + 1 < N:
        #         if nums[i + 1] > nums[i]:
        #             pt = 1
        #         elif nums[i + 1] == nums[i]:
        #             continue
        #         else:
        #             pt = 0
        #     long = 1            
        #     for j in range(i + 1, N):                
        #         if pt and nums[j] > nums[j - 1]:
        #             long += 1
        #             pt = not pt
        #         elif not pt and nums[j] < nums[j - 1]:
        #             long += 1
        #             pt = not pt
        #     ans = max(ans, long)
        # return ans