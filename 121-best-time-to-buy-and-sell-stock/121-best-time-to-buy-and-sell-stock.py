class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _min = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            profit = prices[i] - _min
            ans = max(ans, profit)
            _min = min(_min, prices[i])
        return ans
        # tab = [0 for i in range(len(prices))]
        # for i in range(1, len(tab)):
        #     for j in range(i):
        #         if prices[i] > prices[j]:
        #             tab[i] = max(tab[i], prices[i] - prices[j])
        # return max(tab)
            
            
#         low = prices[0]
#         max_profit = 0
#         for i in range(1, len(prices)):
#             profit = prices[i] - low
#             max_profit = max(max_profit, profit)
#             low = min(prices[i], low)
#         return max_profit
        
        
        # max_profit = 0
        # if len(prices) == 1: return 0
        # l, r = 0, 1
        # while r < len(prices):
        #     if prices[r] >= prices[l]:                
        #         profit = prices[r] - prices[l]
        #         max_profit = max(profit, max_profit)
        #     else:
        #         l = r
        #     r += 1
        # return max_profit
            
# Brute force solution with O(n^2) solution
#         ans = 0
#         for i in range(len(prices)):
#             for j in range(i + 1, len(prices)):
#                 if prices[j] - prices[i] > ans:
#                     ans = prices[j] - prices[i]
                    
#         return ans
        