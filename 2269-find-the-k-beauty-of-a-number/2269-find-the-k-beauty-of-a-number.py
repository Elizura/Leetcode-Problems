class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        l = 0        
        N = len(str(num))
        ans = 0
        for r in range(l + k - 1, N):
            if int(str(num)[l: r + 1]) > 0:
                if not num % int(str(num)[l: r + 1]):
                    ans += 1            
            l += 1
        return ans