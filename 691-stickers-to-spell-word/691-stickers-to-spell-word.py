class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        dp = [-1] * (1 << n)
        dp[0] = 0
        for state in range(1 << n):
            if dp[state] == -1: continue
            for sticker in stickers:
                now = state
                for letter in sticker:
                    for i in range(n):
                        if (now >> i) & 1: continue
                        if target[i] == letter:
                            now |= 1 << i
                            break
                if dp[now] == -1 or dp[now] > dp[state] + 1:
                    dp[now] = dp[state] + 1
        return dp[-1]
