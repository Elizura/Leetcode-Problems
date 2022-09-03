class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
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