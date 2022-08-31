class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        memo = {}
        current = 60 * int(current[:2]) + int(current[3:])        
        correct = 60 * int(correct[:2]) + int(correct[3:])
        target = correct - current
        nums = [1, 5, 15, 60]        
        def dfs(target):
            if target in memo: return memo[target]
            if target == 0: return 0
            if target < 0: return
            smallest = inf
            for i in nums:            
                rem = target - i
                a = dfs(rem)
                if a is not None:                    
                    a += 1
                    if a < smallest:                        
                        smallest = a                        
            memo[target] = smallest            
            return smallest
        
        return dfs(target)
        