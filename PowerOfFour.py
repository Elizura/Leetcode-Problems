class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0:
            return False
        if n==1:
            return True
        elif not n%4:
            return Solution.isPowerOfFour(self,n/4)
        elif n%4:
            return False
