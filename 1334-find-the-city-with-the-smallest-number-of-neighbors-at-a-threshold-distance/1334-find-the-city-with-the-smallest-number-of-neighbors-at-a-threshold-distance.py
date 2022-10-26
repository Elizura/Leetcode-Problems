class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance = [[inf]*n for _ in range(n)]
        for start, end, weight in edges:
            distance[start][start] = 0
            distance[end][end] = 0
            distance[start][end] = weight
            distance[end][start] = weight        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])                 
        ans = []
        reachable_city = [0]*n
        for i in range(n):
            for j in range(n):
                if distance[i][j] <= distanceThreshold:
                    reachable_city[i] += 1
        _min = min(reachable_city)
        for i in range(n - 1, -1, -1):
            if reachable_city[i] == _min:
                return i