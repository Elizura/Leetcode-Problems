class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        visited = [False] * numCourses
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1        
        ancestors = [set() for _ in range(numCourses)]
        q = deque()
        dic = {}
        level = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)                        
        while q:
            for i in range(len(q)):
                a = q.popleft()                
                dic[a] = level
                for n in graph[a]:
                    if not visited[n]:
                        ancestors[n].add(a)
                        ancestors[n].update(ancestors[a])
                        indegree[n] -= 1
                        if indegree[n] == 0:
                            q.append(n)
                            visited[n] = True
            level += 1             
        N = len(queries)
        ans = [False] * N
        for i in range(N):            
            a, b = queries[i]
            if dic[a] < dic[b] and a in ancestors[b]:
                ans[i] = True
        return ans