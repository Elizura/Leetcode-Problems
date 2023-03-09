class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dic = {0: 1}
        pref = 0
        ans = 0
        for num in nums:
            pref += num
            if pref - goal in dic:
                ans += dic[pref - goal]
            dic[pref] = dic.get(pref, 0) + 1
        return ans