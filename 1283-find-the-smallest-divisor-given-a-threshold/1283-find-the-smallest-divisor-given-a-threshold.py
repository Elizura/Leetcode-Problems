class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def calc(divisor):            
            return True if sum([ceil(i/divisor) for i in nums]) <= threshold else False
        
        ans = max(nums)        
        l, r = 1, max(nums)
        
        while r >= l:            
            m = (l + r)//2
            if calc(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
                
                
        return ans
    
        # def enough(threshold, divisor):
        # s = 0
        # for i in nums:
        #     s += (i + divisor - 1) // divisor
        # return s <= threshold
        # l, r = 1, max(nums)
        # while l < r:
        #     m = l + (r - l) // 2
        #     # print(m)
        #     if enough(threshold, m):
        #         r = m
        #     else:
        #         l = m + 1
        # return l
            