class Solution:    
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = [coin for coin in coins if coin <= amount]
        dp = [amount+1]*(amount+1)
        dp[0]=0
        for a in range(1,amount + 1):
            for coin in coins:
                if a-coin >= 0 and dp[a-coin] +1 < dp[a]:
                        dp[a] = dp[a-coin] +1
        return dp[amount] if dp[amount] <amount + 1 else -1
        # tab = [-1 for i in range(amount + 1)]
        # tab[0] = 0
        # for cell in range(len(tab)):
        #     if tab[cell] != -1:
        #         for coin in coins:
        #             if cell + coin < len(tab):
        #                 if tab[cell + coin] != -1:
        #                     if tab[cell] + 1 < tab[cell + coin]:
        #                         tab[cell + coin] = tab[cell] + 1
        #                 else:
        #                     tab[cell + coin] = tab[cell] + 1
        # return tab[-1]
        # coins.sort(reverse = True)
        # ans = 0
        # for i in coins:
        #     while amount >= i:
        #         amount -= i
        #         ans += 1
        # return ans if amount == 0 else -1
            # memo = {}
            # def dfs(coins, amount):             
            #     if amount in memo: return memo[amount]
            #     if amount == 0: return 0
            #     if amount < 0: return None
            #     smallest = -1
            #     for i in coins:            
            #         rem = amount - i
            #         a = dfs(coins, rem)
            #         if a is not None:    
            #             if a > -1:
            #                 a = a + 1
            #                 if smallest == -1: smallest = a                                   
            #                 if a < smallest: smallest = a                
            #     memo[amount] = smallest
            #     return smallest
            # return dfs(coins, amount)