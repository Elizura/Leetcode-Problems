class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(idx, bought):
            if (idx, bought) in memo : return memo[(idx, bought)]
            if idx > len(prices) - 1: return 0
            if idx == len(prices) - 1:
                if bought:
                    return prices[-1]
                else:
                    return 0
            if not bought:
                buy = -prices[idx] + dfs(idx + 1, True)
                skip = dfs(idx + 1, False)
                memo[(idx, bought)] = max(buy, skip)
                return max(buy, skip)
            else:
                sell = prices[idx] + dfs(idx + 1, False)
                skip = dfs(idx + 1, True)
                memo[(idx, bought)] = max(sell, skip)
                return max(sell, skip)
        memo = {}
        memo[(len(prices) - 1, True)] = prices[-1]
        return dfs(0, False)