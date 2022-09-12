class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        def ones(s):
            pref = 0
            ans = 0
            for i in s:
                if int(i) == 1:
                    pref += 1
                    ans = max(ans, pref)
                else:
                    pref = 0
            return ans
        def zeros(s):
            pref = 0
            ans = 0
            for i in s:
                if int(i) == 0:
                    pref += 1
                    ans = max(ans, pref)
                else:
                    pref = 0
            return ans
        wans = ones(s)
        theros = zeros(s)
        return wans > theros