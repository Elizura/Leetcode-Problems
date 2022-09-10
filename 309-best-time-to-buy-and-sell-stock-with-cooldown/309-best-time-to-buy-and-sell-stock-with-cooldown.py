class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(idx, bought, cooldown):
            if cooldown: return dfs(idx + 1, bought, False)
            if (idx, bought) in memo : return memo[(idx, bought)]
            if idx > len(prices) - 1: return 0
            if idx == len(prices) - 1:
                if bought and not cooldown:
                    return prices[-1]
                else:
                    return 0
            if not bought:
                buy = -prices[idx] + dfs(idx + 1, True, False)
                skip = dfs(idx + 1, False, cooldown)
                memo[(idx, bought)] = max(buy, skip)
                return max(buy, skip)
            else:
                sell = prices[idx] + dfs(idx + 1, False, True)
                skip = dfs(idx + 1, True, cooldown)
                memo[(idx, bought)] = max(sell, skip)
                return max(sell, skip)
        memo = {}
        memo[(len(prices) - 1, True)] = prices[-1]
        return dfs(0, False, False)