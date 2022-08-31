class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def convert(t):
            a, b = list(map(int, t.split(':')))
            return 60*a + b
        ret = 0
        # ans = 0
        # memo = {}
        # current = 60 * int(current[:2]) + int(current[3:])        
        # correct = 60 * int(correct[:2]) + int(correct[3:])
        current = convert(current)
        correct = convert(correct)
        target = correct - current
        nums = [60, 15, 5, 1]
        
        for i in nums:
            while target >= i:
                target -= i
                ret += 1
        return ret
                
        
        
        
        
        # i = 0
        # while i < len(nums):        
        #     ans += nums[i]
        #     if ans > target:
        #         ans -= nums[i]
        #         i += 1
        #     else:
        #         ret += 1
        #         if ans == target:
        #             return ret
        # return 0
            
            
#         def dfs(target):
#             if target in memo: return memo[target]
#             if target == 0: return 0
#             if target < 0: return
#             smallest = inf
#             for i in nums:            
#                 rem = target - i
#                 a = dfs(rem)
#                 if a is not None:                    
#                     a += 1
#                     if a < smallest:                        
#                         smallest = a                        
#             memo[target] = smallest            
#             return smallest
        
#         return dfs(target)
        