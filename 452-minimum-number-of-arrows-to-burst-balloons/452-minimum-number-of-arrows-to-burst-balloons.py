class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        shots = 1
        points.sort()
        a = points[0]
        for i, j in points[1:]:
            if i > a[1]:
                shots += 1
                a = [i, j]
            else:                
                a[1] = min(a[1], j)              
        return shots
        