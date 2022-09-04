class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dfs(amt, idx, memo = {}):
            if (idx, amt) in memo: return memo[(idx, amt)]
            if amt == amount: return 1
            if amt > amount: return 0
            if idx >= len(coins): return 0
            memo[(idx, amt)] = dfs(coins[idx] + amt, idx) + dfs(amt, idx + 1)
            return memo[(idx, amt)]
        return dfs(0, 0)