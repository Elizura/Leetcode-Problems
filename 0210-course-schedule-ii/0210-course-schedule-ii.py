class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def topo(node):
            visited[node] = True
            ans.append(node)
            for n in graph[node]:
                indegree[n] -= 1
                if not visited[n] and indegree[n] == 0:
                    topo(n)
            
        ans = []
        indegree = [0] * numCourses
        visited = [False] * numCourses        
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        for i in range(numCourses):
            if indegree[i] == 0 and not visited[i]:
                topo(i)         
        return ans if len(ans) == numCourses else []
                    
            
#         rec = [False] * numCourses
#         visited = [False] * numCourses
#         def topo(node):                        
#             visited[node] = True
#             rec[node] = True
#             for n in graph[node]:
#                 if visited[neighb] == False:
#                     if not checkcyc(neighb): return []                    
#                 elif rec[neighb]: return False
#             rec[node] = False
#             return False
            
#         graph = defaultdict(list)
        
        
        # topo = []
        # graph = defaultdict(list)
        # indegree = [0] * numCourses
        # for a, b in prerequisites:
        #     graph[b].append(a)
        # for c, _ in prerequisites:
        #     indegree[c] += 1
        # q = deque()
        # seen = set()
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         q.append(i)
        #         seen.add(i)
        # while q:
        #     a = q.popleft()
        #     topo.append(a)
        #     for node in graph[a]:
        #         indegree[node] -= 1
        #         if indegree[node] == 0:
        #             q.append(node)
        #             seen.add(node)
        # return topo if len(topo) == numCourses else []