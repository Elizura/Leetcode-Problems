class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) == 1: return 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] >= prices[l]:                
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l = r
            r += 1
        return max_profit
            
                
#         ans = 0
#         for i in range(len(prices)):
#             for j in range(i + 1, len(prices)):
#                 if prices[j] - prices[i] > ans:
#                     ans = prices[j] - prices[i]
                    
#         return ans
        