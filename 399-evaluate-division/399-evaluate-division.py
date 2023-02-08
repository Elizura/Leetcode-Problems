class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def bfs(source, target, value):
            queue = [[source, value]]
            visited = set()
            while queue:
                
                node, val = queue.pop(0)
                if node == target:
                    return val
                if node in visited:
                    continue
                visited.add(node)
                
                for baju_wala in graph[node]:
                    if baju_wala not in visited:
                        new_val = val * graph[node][baju_wala]
                        queue.append([baju_wala, new_val])
            
            return float(-1)
                
        
        graph = {}
        for i in range(len(values)):
            u, v = equations[i]
            value = values[i]
            rev_value = 1 / value
            if u in graph:
                graph[u][v] = value
            else:
                graph[u] = {v: value}
            if v in graph:
                graph[v][u] = rev_value
            else:
                graph[v] = {u: rev_value}
        
        
        result = []
        for a, b in queries:
            if a not in graph or b not in graph:
                result.append(float(-1))
            else:
                res = bfs(a, b, 1)
                result.append(res)
                
        
        return result
            