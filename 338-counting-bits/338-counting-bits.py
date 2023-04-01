class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):            
            ct = 0
            for j in range(32):
                if (1 << j) & i != 0:
                    ct += 1
            ans.append(ct)
        return ans