class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
#         temp = [(num, idx) for idx, num in enumerate(nums)]
#         temp.sort()  
#         ans = 0
#         min_idx = inf
#         for num, idx in temp:
#             ans = max(ans, idx - min_idx)
#             min_idx = min(min_idx, idx)
#         return ans
    
    




            minindex = []
            minval = nums[0]
            ans = 0
            for i,num in enumerate(nums):
                if num <= minval:
                    minindex.append(i)
                    minval = num

            for i in range(len(nums)-1,-1,-1):            
                while minindex and nums[minindex[-1]] <= nums[i]:
                    ans = max(ans,i-minindex.pop())
            return ans













