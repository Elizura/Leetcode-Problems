class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        l = 0
        r = l + k - 1
        N = len(str(num))
        ans = 0
        while r < N:
            if int(str(num)[l: r + 1]) > 0:
                if not num % int(str(num)[l: r + 1]):
                    ans += 1
            r += 1
            l += 1
        return ans