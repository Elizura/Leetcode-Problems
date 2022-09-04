class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # cnt = [1 for i in range(len(nums))]
        # tab = [1 for i in range(len(nums))]
        # for i in range(1, len(tab)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             if tab[j] + 1 == tab[i]:
        #                 cnt[i] += cnt[j]
        #             tab[i] = max(tab[j] + 1, tab[i])
        # print(cnt)
        # a = max(tab) 
        # ans = 0
        # for i in range(len(tab)):
        #     if tab[i] == a:
        #         ans += cnt[i]
        # return ans
    
        dp = [1] * len(nums)
        cnt = [1] * len(nums)
        
        maxSoFar = 1
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]
                        
            maxSoFar = max(maxSoFar, dp[i])
            
        nos = 0
        for i in range(len(nums)):
            if dp[i] == maxSoFar:
                nos += cnt[i]
                
        return nos