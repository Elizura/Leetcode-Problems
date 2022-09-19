class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        connections = {(a, b) for a, b in connections}
        ans = 0
        neighbors = {city:[] for city in range(n)}
        for i, j in connections:
            neighbors[i].append(j)
            neighbors[j].append(i)
            
        seen = set()
        def dfs(city):
            nonlocal ans
            for neighbor in neighbors[city]:
                if neighbor in seen: continue
                if (neighbor, city) not in connections:                    
                    ans += 1
                seen.add(neighbor)
                dfs(neighbor)
            
        seen.add(0)
        dfs(0)
        return ans