class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        l, r = 0, max(nums)
        
        
        def helper(n):            
            l, r = 0, len(nums) - 1
            while r >= l:
                m = (l + r)//2                
                if nums[m] >= n:
                    r = m - 1
                else:
                    l = m + 1                
                    
            return len(nums) - l
        
        
        while r >= l:
            m = (r + l)//2
            a = helper(m)            
            if a == m: return m            
            elif a > m:
                l = m + 1
            else: #a < b
                r = m - 1
        return -1 