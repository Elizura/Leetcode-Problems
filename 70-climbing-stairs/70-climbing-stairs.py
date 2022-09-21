class Solution:    
    def climbStairs(self, n: int) -> int:
        def dfs(n):
            if n < 0: return 0
            if dp[n] != None: return dp[n]
            if n == 0: return 1
            dp[n] = dfs(n - 1) + dfs(n - 2)
            return dp[n]
        dp = [None for i in range(n + 1)]
        return dfs(n)
    #     cur = 0
    #     a, b = 0, 1
    #     for i in range(1, n + 1):
    #         a, b = b, b + a
            # cur = b + a
            # a = b
            # b = cur            
        return b

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


# class Solution:
#     dic = {}
#     def climbStairs(self, n: int) -> int:        
#         if n in self.dic: return self.dic[n]
#         if n <= 1: return 1        
#         self.dic[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
#         return self.dic[n]        


