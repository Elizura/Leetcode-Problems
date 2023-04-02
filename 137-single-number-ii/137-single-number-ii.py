class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0                
        for i in range(32):
            var = 0
            for num in nums:                                                                       
                if num >> i & 1:
                    var += 1
            var %= 3            
            if var and i == 31: 
                ans -= 1 << 31  
                continue                
            if var:
                ans |= (1 << i)
        return ans
    
