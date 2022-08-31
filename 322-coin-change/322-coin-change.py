class Solution:    
    def coinChange(self, coins: List[int], amount: int) -> int:  
            memo = {}
            def dfs(coins, amount):             
                if amount in memo: return memo[amount]
                if amount == 0: return 0
                if amount < 0: return None
                smallest = -1
                for i in coins:            
                    rem = amount - i
                    a = dfs(coins, rem)
                    if a is not None:    
                        if a > -1:
                            a = a + 1
                            if smallest == -1: smallest = a                                   
                            if a < smallest: smallest = a                
                memo[amount] = smallest
                return smallest
            return dfs(coins, amount)