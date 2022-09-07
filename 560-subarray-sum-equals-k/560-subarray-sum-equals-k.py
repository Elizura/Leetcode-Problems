class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = 0
        dic = {0: 1}
        ans = 0
        for i in nums:
            pref += i
            if pref - k in dic:
                ans += dic[pref - k]                
            if pref in dic:
                dic[pref] += 1
            if pref not in dic: dic[pref] = 1
        return ans            