class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ind = nums.index(k)
        backG, backS = 0, 0
        forG, forS = 0, 0
        dic = defaultdict(int)
        ans = 0
        for i in range(ind - 1, -1, -1):
            if nums[i] > k: backG += 1
            else: backS += 1
            dic[backG - backS] += 1
            if backG == backS or backG - backS == 1: ans += 1
        for i in range(ind + 1, len(nums)):
            if nums[i] > k: forG += 1
            else: forS += 1
            ans += dic[forS - forG] + dic[forS - forG + 1]
            if forG == forS or forG - forS == 1: ans += 1
        return ans + 1

            