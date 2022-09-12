class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        pref = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                pref += 1
                ans = max(ans, pref)
            else:
                pref = 1
        return ans
            