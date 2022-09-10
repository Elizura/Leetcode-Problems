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
                memo[(idx, bought)] = max(-prices[idx] + dfs(idx + 1, True), dfs(idx + 1, False))
                return memo[(idx, bought)]
            else:
                memo[(idx, bought)] = max(prices[idx] + dfs(idx + 1, False), dfs(idx + 1, True))
                return memo[(idx, bought)]
        memo = {}
        memo[(len(prices) - 1, True)] = prices[-1]
        return dfs(0, False)