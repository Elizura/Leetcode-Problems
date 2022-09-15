class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canship(capacity):            
            day = 1
            capa = capacity
            i = 0
            while i < len(weights):
                if capa >= weights[i]:
                    capa -= weights[i]
                    i += 1
                else:
                    day += 1
                    capa = capacity                                            
            return day <= days
        
        least, last, ans = max(weights), sum(weights), max(weights)
        while last >= least:
            mid = (last + least)//2
            if canship(mid):                 
                ans = mid                
                last = mid -1
            else:
                least = mid + 1
        return ans