class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        seen, banned = set(), [False] * n
        ban_d = ban_r = 0
        while len(seen) != 1:
            seen = set()
            for i, p in enumerate(senate):
                if banned[i]: continue
                if p == 'R':
                    if ban_r > 0:          
                        ban_r -= 1
                        banned[i] = True
                    else:                   
                        ban_d += 1
                        seen.add('R')
                else:        
                    if ban_d > 0:
                        ban_d -= 1
                        banned[i] = True
                    else:
                        ban_r += 1
                        seen.add('D')
        return 'Radiant' if seen.pop() == 'R' else 'Dire'