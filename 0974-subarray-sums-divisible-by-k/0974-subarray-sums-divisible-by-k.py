class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        pref = 0
        ans = 0
        for num in nums:
            pref += num
            t = pref % k
            if t in dic:
                a = dic[t]
                ans += a
                dic[t] = a + 1
            else:
                dic[t] = 1
        return ans    
    
# class Solution:
#     def subarraysDivByK(self, A, K):
#         csum, ans = 0, 0
#         D = [0] * K
#         D[0] = 1
#         for i in A:
#             csum = (csum + i) % K
#             ans += D[csum]
#             D[csum] += 1
#         return ans