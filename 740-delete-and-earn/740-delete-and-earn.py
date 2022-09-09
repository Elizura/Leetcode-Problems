class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        nums = list(set(nums))
        a, b = 0, 0
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] + 1:
                a, b = b, max(b, a + nums[i] * cnt[nums[i]])
            else:
                a, b = b, b + nums[i] * cnt[nums[i]]
        return b
        
        
        
#         count = collections.Counter(nums)
#         nums = list(set(nums))
#         def dfs(idx):
#             if dp[idx] != 0: return dp[idx]
#             if idx < 0: return 0
#             if idx == 0: return dp[0]
#             if nums[idx] == nums[idx - 1] + 1:
#                 take = dfs(idx - 2) + nums[idx]*count[nums[idx]]
#                 not_take = dfs(idx - 1)
#                 dp[idx] = max(take, not_take)
#                 return dp[idx]
#             if nums[idx] > nums[idx - 1] + 1:                                
#                 dp[idx] = dfs(idx - 1) + nums[idx]*count[nums[idx]]
#                 return dp[idx]
#         dp = [0 for i in range(len(nums))]
#         dp[0] = nums[0]*count[nums[0]]
#         return dfs(len(nums) - 1)
            
            
        count = collections.Counter(nums)
        nums = list(set(nums))
        a, b = 0, 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] + 1:
                a, b = b, max(a + nums[i] * count[nums[i]], b)
            else:
                a, b = b, b + nums[i] * count[nums[i]]
        return b
        
#         count = collections.Counter(nums)
#         nums = list(set(nums))
#         nums.sort()
#         tab = [0 for i in nums]
#         tab[0] = nums[0]*count[nums[0]]
#         for i in range(1, len(nums)):            
#             if nums[i] == nums[i - 1] + 1:
#                 if i - 2 >= 0:
#                     tab[i] = max(tab[i - 2] + nums[i] * count[nums[i]], tab[i - 1])
#                 else:
#                     tab[i] = max(nums[i]*count[nums[i]], tab[i - 1])
#             elif nums[i] > nums[i - 1] + 1:
#                 tab[i] = tab[i - 1] + nums[i]*count[nums[i]]            
#         return tab[-1]
        
        
#         c, res, r=collections.Counter(nums), 0, 0
#         for i in set(c):
#             if not c[i-1]: l, r, res = 0,0,res + r
#             l, r= r, max(l + c[i]*i, r)
        # return (res + r)
    
    
#         def dfs(idx, amt, memo = {}):
#             if (idx, amt) in memo: return memo[(idx, amt)]
#             if idx >= len(nums): return amt
#             if idx + 1 < len(nums):
#                 if nums[idx + 1] == nums[idx] + 1:
#                     include = dfs(idx + 2, amt + nums[idx]*count[nums[idx]], memo)
#                     disclude = dfs(idx + 1, amt, memo)
#                 elif nums[idx + 1] > nums[idx] + 1:
#                     include = dfs(idx + 1, amt + nums[idx]*count[nums[idx]], memo)
#                     disclude = dfs(idx + 1, amt, memo)
#             elif idx + 1 >= len(nums): 
#                 include = amt + nums[idx] *count[nums[idx]]
#                 disclude = amt 
#             memo[(idx, amt)] = max(include, disclude)
#             return memo[(idx, amt)]        
#         count = collections.Counter(nums)
#         nums = list(set(nums))
#         nums.sort()        
#         return dfs(0, 0)

        
#         count = Counter(nums)
#         m = max(nums)
#         memo = {}
#         def choose(num):
#             if num > m:
#                 return 0
#             if num not in count:
#                 count[num] = 0
#             if num in memo:
#                 return memo[num]
#             memo[num] = max(choose(num + 1), num * count[num] + choose(num + 2))
#             return memo[num]
        
#         return choose(1)