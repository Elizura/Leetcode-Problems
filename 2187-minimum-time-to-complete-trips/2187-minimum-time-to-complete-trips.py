class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:        
        def cantrip (timee):
            trips = 0
            for i in time:
                if i <= timee:
                    trips += timee//i
            return trips >= totalTrips
        l, r = 1, min(time)*totalTrips
        while r > l:
            m = (l + r) // 2
            if cantrip(m):
                r = m 
            else:
                l = m + 1
        return l