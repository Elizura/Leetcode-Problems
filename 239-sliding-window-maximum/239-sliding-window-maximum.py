class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        for idx, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(idx)
            
            if q[0] == idx - k:
                q.popleft()
            
            if idx >= k - 1:
                ans.append(nums[q[0]])
        return ans
        


        
        
        
        
        