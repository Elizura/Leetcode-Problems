class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = collections.Counter(s1)
        def check(s1, t):            
            temp = collections.Counter(t)            
            for i in s1:
                if i not in temp: return False
                if i in temp and temp[i] != count[i]: return False                           
            return True
        l, r, N = 0, len(s1) - 1, len(s2)
        while r < N:            
            if check(s1, s2[l:r + 1]): return True
            r += 1
            l += 1
        return False