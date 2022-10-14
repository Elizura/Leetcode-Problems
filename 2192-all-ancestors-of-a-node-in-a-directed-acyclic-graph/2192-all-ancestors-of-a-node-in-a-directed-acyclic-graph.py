class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:   
        graph = defaultdict(list)
        indegree = [0] * n
        for a, b in edges:
            graph[a].append(b)   
            indegree[b] += 1        
        ans = [set() for _ in range(n)]             
        q = deque()
        visited = [False] * n
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)                        
        while q:
            a = q.popleft()
            for n in graph[a]:                
                if not visited[n]:
                    ans[n].add(a)
                    ans[n].update(ans[a])
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        q.append(n)
                        visited[n] = True 
        ans = [sorted(list(s)) for s in ans]
        return ans