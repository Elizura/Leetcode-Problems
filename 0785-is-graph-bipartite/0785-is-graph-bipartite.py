class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs(ver):
            color = [-1] * len(graph)
            q = deque([ver])
            color[ver] = 1
            while q:
                a = q.popleft()
                seen.add(a)
                for node in graph[a]:
                    if color[node] == -1:
                        color[node] = 1 - color[a]
                        q.append(node)
                    else:
                        if color[node] == color[a]: return False
            return True
        
        seen = set()
        for i in range(len(graph)):
            if i not in seen:
                if not bfs(i): return False
        return True