class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        stack=[]
        curr=0
        for i in range(n):
            stack.append(i+1)
        while n>1:
            stack.pop(((curr-1+k)%n))
            curr=(curr-1+k)%n
            n-=1
        return stack[-1]
