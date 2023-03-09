class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ct = Counter(t)
        cs = {}
        left = 0
        got = 0
        need = len(set(t))
        ans = inf
        l, r = -1, -1
        for right in range(len(s)):
            cs[s[right]] = cs.get(s[right], 0) + 1
            if s[right] in ct and ct[s[right]] == cs[s[right]]:
                got += 1
            while got == need:                
                if right - left + 1 < ans:
                    ans = right - left + 1
                    l, r = left, right                
                cs[s[left]] -= 1  
                if s[left] in ct and cs[s[left]] < ct[s[left]]:
                    got -= 1
                if not cs[s[left]]: del cs[s[left]]
                left += 1
        return s[l: r + 1]
                