class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        @cache
        def dfs(l, r):
            N = len(piles)
            if l > r: return 0
            turn = N - (r - l + 1)
            if not turn % 2: #Alice turn
                return max(piles[l] + dfs(l + 1, r), piles[r] + dfs(l, r - 1))
            else: #Bob's turn 
                return max(-piles[l] + dfs(l + 1, r), -piles[r] + dfs(l, r - 1))
        return dfs(0, N - 1) > 0