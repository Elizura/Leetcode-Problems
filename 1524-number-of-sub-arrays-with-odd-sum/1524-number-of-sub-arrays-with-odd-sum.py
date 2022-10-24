class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd, even = 0, 1
        pref = 0
        N = len(arr)
        ans = 0
        mod = (10 ** 9) + 7
        for num in arr:
            pref += num
            if pref % 2:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1
        return ans % mod