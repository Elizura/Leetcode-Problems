class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # @cache
        # def dfs(choices, remainder):
        #     if choices[-1] >= remainder: return True
        #     for i in range(len(choices)):
        #         if not dfs(choices[:i]+choices[i+1:], remainder - choices[i]):
        #             return True
        #     return False
        # total = (maxChoosableInteger + 1)*maxChoosableInteger/2
        # if total < desiredTotal: return False
        # choices = tuple(range(1,maxChoosableInteger + 1))
        # return dfs(choices, desiredTotal)
        
        @cache        
        def dfs(choises, amt):            
            if choises[-1] >= amt: return True
            for i, v in enumerate(choises):
                res = dfs(choises[:i] + choises[i + 1:], amt - v)
                if not res:                    
                    return True                
            return False
        tot = (maxChoosableInteger + 1) * maxChoosableInteger / 2
        if tot < desiredTotal: return False
        nums = tuple((range(1, maxChoosableInteger + 1)))
        return dfs(nums, desiredTotal)