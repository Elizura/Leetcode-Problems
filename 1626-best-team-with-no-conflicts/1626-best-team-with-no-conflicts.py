class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # a = []
        # temp = []
        # for i in range(len(ages)):
        #     temp.append((ages[i], scores[i]))
        # temp.sort()
        # for i in temp:
        #     a.append(i[1])
        # dp = [i for i in a]
        # for i in range(len(dp)):
        #     for j in range(i):
        #         print(dp)
        #         if a[i] >= a[j]:
        #             dp[i] = max(dp[i], dp[j] + a[i])
        # return max(dp)
        
#         players = list(zip(ages,scores))
#         players.sort()
#         N = len(players)
                
#         dp = [players[i][1] for i in range(N)]
#         for j in range(N):
#             for i in range(j):			    
#                 if players[i][1] <= players[j][1]:
#                     dp[j] = max(dp[j], dp[i] + players[j][1])
#         return max(dp)
        a = []
        least = []
        for i in range(len(ages)):
            least.append((ages[i], scores[i]))
        least.sort()
        for i in least:
            a.append(i[-1])
        tab = [i for i in a]        
        for i in range(1, len(tab)):         
            for j in range(i):                
                if a[i] >= a[j]:                    
                    tab[i] = max(tab[i], tab[j] + a[i])        
        return max(tab)
    
                        
        # dp = [players[i][1] for i in range(N)]
        # for j in range(N):
        #     for i in range(j):			    
        #         if players[i][1] <= players[j][1]:
        #             dp[j] = max(dp[j], dp[i] + players[j][1])
        # return max(dp)