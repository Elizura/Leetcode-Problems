class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        pref = 0
        ans = 0
        for num in nums:
            pref += num
            if pref - k in dic:
                ans += dic[pref - k]
            if pref in dic:
                dic[pref] += 1
            if pref not in dic:
                dic[pref] = 1
        return ans