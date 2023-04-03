class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:     
        xor = 0
        for num in nums:
            xor ^= num
        k = 0
        for i in range(32):
            if (1 << i) & xor:
                k = i                                    
                
        xor1 = 0
        xor2 = 0
        for num in nums:            
            if num & (1 << k):
                xor1 ^= num                
            else:
                xor2 ^= num
                
        return [xor1, xor2]