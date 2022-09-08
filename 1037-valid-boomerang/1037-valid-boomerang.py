class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0][0], points[0][1]
        x2, y2 = points[1][0], points[1][1]
        x3, y3 = points[2][0], points[2][1]
        
        slope1 = (y2 - y1)*(x3 - x2)
        slope2 = (y3 - y2)*(x2 - x1)
        return not (slope1 == slope2)