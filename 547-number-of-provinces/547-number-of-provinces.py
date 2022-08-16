class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        provinces = 0
        def dfs(city):
            if city in seen: return 
            seen.add(city)
            for j in range(len(isConnected[0])):
                if isConnected[city][j] == 1:                    
                    dfs(j)                
        for city in range(len(isConnected)):
            if city not in seen:
                dfs(city)
                provinces += 1
        return provinces
        