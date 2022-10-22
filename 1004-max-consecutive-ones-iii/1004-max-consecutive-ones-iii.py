class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        ans = 0
        N = len(nums)
        while right < N:
            while right < N and k >= 0:
                if nums[right] == 0 and k == 0:
                    k -= 1
                    continue
                if nums[right] == 0 and k > 0:
                    k -= 1
                ans = max(ans, right - left + 1)
                right += 1
            if nums[left] == 0:
                k += 1
            left += 1
            right += 1
            if right < N and nums[right] == 0:
                k -= 1
        return ans
            
#         l=0
#         r=0
#         ans=0
#         ans_=0
#         while r<len(nums):
#             while k>=0 and r<len(nums):
#                 if nums[r]==1:
#                     ans_= r-l+1
#                 elif nums[r] == 0 and k==0:
#                     k-=1
#                 elif nums[r]==0:
#                     ans_=r-l+1
#                     k-=1
#                 r+=1
#             if ans_>ans:
#                 ans=ans_
#             if nums[l]==0:
#                 l+=1
#                 k+=1
#             elif nums[l]==1:
#                 l+=1

#             ans_=0
#         return ans