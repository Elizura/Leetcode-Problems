class Solution:
    # dic = {}
    def fib(self, n: int) -> int:
        if n == 0: return 0
        dp = [0] * (n + 1)        
        dp[0], dp[1] = 0, 1
        for i in range(n + 1):
            if i + 1 <= n: dp[i + 1] += dp[i]
            if i + 2 <= n: dp[i + 2] += dp[i]
        return dp[-1]
            
#         if n in self.dic: return self.dic[n]
#         if n == 0: return 0
#         if n <= 2: return 1
#         self.dic[n] = self.fib(n - 1) + self.fib(n - 2)
#         return self.dic[n]
        