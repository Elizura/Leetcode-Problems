class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '': return ''
        l = 0
        countT, win = collections.Counter(t), {}
        have, want = 0, len(countT)
        ans_ind, ans_len = [-1, -1], inf
        for r in range(len(s)):
            c = s[r]
            win[c] = win.get(c, 0) + 1
            if c in countT and countT[c] == win[c]:
                have += 1
            while have == want:
                if (r - l + 1) < ans_len:
                    ans_ind, ans_len = [l, r], (r - l + 1)
                win[s[l]] -= 1
                if s[l] in countT and win[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = ans_ind
        return s[l: r + 1] if ans_len != inf else ''