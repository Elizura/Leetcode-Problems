class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:  
        stack = [] #store the damn index
        N = len(nums)
        ans = [-1] * N
        for i in range(2 * N - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % N]:
                stack.pop()
            if stack:
                ans[i % N] = nums[stack[-1]]
            stack.append(i % N)
        return ans
        # N = len(nums)
        # temp = nums + nums
        # ans = [-1] * N
        # stack = [] #stores an index
        # for idx, num in enumerate(temp):
        #     while stack and num > nums[stack[-1]]:
        #         a = stack.pop()
        #         ans[a % N] = num
        #     stack.append(idx % N)
        # return ans