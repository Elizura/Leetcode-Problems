class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:        
        N = len(nums)
        temp = nums + nums
        ans = [-1] * N
        stack = [] #stores an index
        for idx, num in enumerate(temp):
            while stack and num > nums[stack[-1]]:
                a = stack.pop()
                ans[a % N] = num
            stack.append(idx % N)
        return ans