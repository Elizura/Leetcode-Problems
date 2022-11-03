class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        prev_min = inf
        stack = [] #(num, prev_min)        
        for num in nums:
            while stack and num >= stack[-1][0]:
                stack.pop()
            if stack and num > stack[-1][1]:
                return True
            stack.append([num, prev_min])
            prev_min = min(prev_min, num)
        return False