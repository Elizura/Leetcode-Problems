class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #base case
        if n==0:
            return False
        if n==1:
            return True
        elif not n%3:
            return Solution.isPowerOfThree(self,n/3)
        elif n%3:
            return False
