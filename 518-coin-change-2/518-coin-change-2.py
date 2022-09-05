class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        tab = [[0 for i in range(amount + 1)] for i in range(len(coins))]
        for i in range(len(coins)):
            tab[i][0] = 1
        for i in range(len(coins)):
            for j in range(1, amount + 1):
                if coins[i] <= j:
                    if i - 1 >= 0:                        
                        tab[i][j] = tab[i - 1][j] + tab[i][j - coins[i]]
                    else:
                        tab[i][j] = tab[i][j - coins[i]]
                else:
                    tab[i][j] = tab[i - 1][j]
        return tab[-1][-1]
    