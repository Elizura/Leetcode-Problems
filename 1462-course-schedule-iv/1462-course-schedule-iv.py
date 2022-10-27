class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        connected = [[False] * n for i in range(n)]

        for i, j in prerequisites:
            connected[i][j] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    connected[i][j] = connected[i][j] or (connected[i][k] and connected[k][j])

        return [connected[i][j] for i, j in queries]
        # graph = defaultdict(list)
        # visited = [False] * numCourses
        # indegree = [0] * numCourses
        # for a, b in prerequisites:
        #     graph[a].append(b)
        #     indegree[b] += 1        
        # ancestors = [set() for _ in range(numCourses)]
        # q = deque()
        # # dic = {}
        # # level = 0
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         q.append(i)                        
        # while q:
        #     for i in range(len(q)):
        #         a = q.popleft()                
        #         # dic[a] = level
        #         for n in graph[a]:
        #             if not visited[n]:
        #                 ancestors[n].add(a)
        #                 ancestors[n].update(ancestors[a])
        #                 indegree[n] -= 1
        #                 if indegree[n] == 0:
        #                     q.append(n)
        #                     visited[n] = True
        #     # level += 1             
        # N = len(queries)
        # ans = [False] * N
        # for i in range(N):            
        #     a, b = queries[i]
        #     if a in ancestors[b]:
        #         ans[i] = True
        # return ans