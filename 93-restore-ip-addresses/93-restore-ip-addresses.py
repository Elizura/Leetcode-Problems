class Solution:
    def works(self, s):
        return s == str(int(s)) and int(s) <= 255

    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        for i in range(1, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
                    if self.works(a) and self.works(b) and self.works(c) and self.works(d):
                        ans.append(f'{a}.{b}.{c}.{d}')
        return ans