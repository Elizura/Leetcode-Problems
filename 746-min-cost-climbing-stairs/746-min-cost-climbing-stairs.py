class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = cost[0], cost[1]
        for i in range(2, len(cost)):
            a, b = b, min(a + cost[i], b + cost[i])
        return min(a, b)
        # dp = [0 for i in range(len(cost))]
        # dp[0] = cost[0]
        # dp[1] = cost[1]
        # for i in range(2, len(cost)):
        #     dp[i] = min(dp[i - 2] + cost[i], dp[i - 1] + cost[i] )
        # return min(dp[-1], dp[-2])