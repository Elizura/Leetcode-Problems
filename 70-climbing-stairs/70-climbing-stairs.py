# class Solution:    
#     def climbStairs(self, n: int) -> int:
#         storage = {}
#         if n <= 2:
#             storage[n] = n 
#             return n 
#         if n in storage:
#             return storage[n]
#         else :
#             while n > 2:
#                 storage [n] = self.climbStairs(n-1) + self.climbStairs(n-2)
#                 return storage[n]


class Solution:
    dic = {}
    def climbStairs(self, n: int) -> int:        
        if n in self.dic: return self.dic[n]
        if n <= 1: return 1        
        self.dic[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dic[n]        