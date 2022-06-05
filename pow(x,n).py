class Solution:
    def myPow(self, x: float, n: int) -> float:
            if x==0:
                return 0
            if n==0:
                return 1

            elif n>0 and not n%2:
                temp=Solution.myPow(self,x,n/2)
                ans= temp*temp
                return ans
            elif n>0 and n%2:
                return x*Solution.myPow(self,x,n-1)
            elif n<0:
                n=-1*n
                if not n%2:
                    temp=Solution.myPow(self,1/x,n/2)
                    ans=temp*temp
                elif n%2:
                    return x*Solution.myPow(self,1/x,n+1)
            return ans
