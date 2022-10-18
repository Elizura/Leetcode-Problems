class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tot_sum = sum(nums)
        if not tot_sum % p: return 0
        target = tot_sum % p
        pref = 0
        ans = inf
        dic = {0: -1}
        for idx, num in enumerate(nums):
            pref = (pref + num) % p
            dic[pref] = idx                            
            if (pref - target) % p in dic:
                ans = min(ans, idx - dic[(pref - target) % p])                
        return ans if ans < len(nums) else -1
    
    