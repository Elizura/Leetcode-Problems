class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        pref = 0
        ans = 0
        for num in nums:
            pref += num
            t = pref % k
            if t in dic:                
                ans += dic[t]
                dic[t] += 1
            else:
                dic[t] = 1
        return ans    
    
