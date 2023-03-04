class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:  
        n = len(nums)
        nextG = [n]*n
        prevG = [-1]*n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                ind = stack.pop()
                nextG[ind] = i
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                ind = stack.pop()
                prevG[ind] = i
            stack.append(i)
        ans = 0
        for i in range(n):
            if left <= nums[i] <= right:
                l = i - prevG[i] - 1
                r = nextG[i] - i - 1
                lr = l*r
                ans += (l + r + lr) + 1                 
        return ans