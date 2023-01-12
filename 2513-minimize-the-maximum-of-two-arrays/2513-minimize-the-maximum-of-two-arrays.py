class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def isvalid(n):
            a = n//divisor1
            b = n//divisor2
            c = n//math.lcm(divisor1, divisor2)
            if n - a < uniqueCnt1: return False
            if n - b < uniqueCnt2: return False
            if n - c < (uniqueCnt1 + uniqueCnt2): return False
            return True
        l, r = 1, 10**12
        while r >= l:
            m = (r + l)//2
            if isvalid(m):    
                print(m)            
                r = m - 1
            else:
                l = m + 1
        return l