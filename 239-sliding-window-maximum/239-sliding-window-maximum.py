# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         ans = []
#         q = deque()
#         for idx, num in enumerate(nums):
#             while q and nums[q[-1]] < num:
#                 q.pop()
#             q.append(idx)
            
#             if q[0] == idx - k:
#                 q.popleft()
            
#             if idx >= k - 1:
#                 ans.append(nums[q[0]])
#         return ans
        
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        q = deque([])
        
        for right in range(k):
            while q and q[-1][0] <= nums[right]:
                q.pop()
            q.append((nums[right], right))
    
        ans = []
        for idx in range(right+1, len(nums)):            
            ans.append(q[0][0])
            left += 1
            while q and q[-1][0] <= nums[idx]:
                q.pop()
            q.append((nums[idx], idx))
            
            if q[0][1] < left:
                q.popleft()
                
        ans.append(q[0][0])
        return ans


        
        
        
        
        