class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) == 1: return 0
        l, r = 0, 1
        while l < len(prices) and r < len(prices):
            if prices[l] >= prices[r]:
                l = r
                r += 1
                continue
            profit = prices[r] - prices[l]
            if  profit > max_profit: max_profit = profit
            r += 1
        return max_profit
            
                
#         ans = 0
#         for i in range(len(prices)):
#             for j in range(i + 1, len(prices)):
#                 if prices[j] - prices[i] > ans:
#                     ans = prices[j] - prices[i]
                    
#         return ans
        