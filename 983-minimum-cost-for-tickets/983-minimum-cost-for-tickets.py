class Solution:
    def mincostTickets(self, days: List[int], cost: List[int]) -> int:
        days = set(days)    
        @cache
        def dfs(day):
            if day > 365: return 0
            if day not in days: return dfs(day + 1)
            return min((dfs(day + 1) + cost[0]), (dfs(day + 7) + cost[1]), (dfs(day + 30) + cost[2]))
        return dfs(0)