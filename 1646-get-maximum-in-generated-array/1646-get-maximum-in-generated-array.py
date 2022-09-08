class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        dp = [0 for i in range(n + 1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(1, len(dp)):
            if i * 2 < len(dp):
                dp[i * 2] = dp[i]
            if i * 2 + 1 < len(dp):
                dp[(i * 2) + 1] = dp[i] + dp[i + 1]
        return max(dp)
            
        