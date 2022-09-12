class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        maxonecount = 0
        onecount = 0
        maxzerocount = 0
        zerocount = 0
        for char in s:
            if char == '1':
                onecount += 1
                maxonecount = max(maxonecount, onecount)
                zerocount = 0
            else:
                zerocount += 1
                maxzerocount = max(maxzerocount, zerocount)
                onecount = 0
        return maxonecount > maxzerocount
        # def ones(s):
        #     pref = 0
        #     ans = 0
        #     for i in s:
        #         if int(i) == 1:
        #             pref += 1
        #             ans = max(ans, pref)
        #         else:
        #             pref = 0
        #     return ans
        # def zeros(s):
        #     pref = 0
        #     ans = 0
        #     for i in s:
        #         if int(i) == 0:
        #             pref += 1
        #             ans = max(ans, pref)
        #         else:
        #             pref = 0
        #     return ans
        # wans = ones(s)
        # theros = zeros(s)
        # return wans > theros