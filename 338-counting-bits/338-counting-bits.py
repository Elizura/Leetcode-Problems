class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):            
            ct = 0
            j = 0
            while 1 << j <= i:            
                if (1 << j) & i != 0:
                    ct += 1
                j += 1
            ans.append(ct)
        return ans