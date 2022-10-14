class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        topo = []
        ind = [0] * numCourses
        seen = [False] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)        
        for a, _ in prerequisites:
            ind[a] += 1
        q = deque()
        for i in range(numCourses):
            if ind[i] == 0:
                seen[i] = True
                q.append(i)
        while q:
            a = q.popleft()
            topo.append(a)
            for n in graph[a]:
                if not seen[n]:
                    ind[n] -= 1
                    if ind[n] == 0:
                        q.append(n)
                        seen[n] = True 
                                
        return len(topo) == numCourses
        # can = [False for _  in range(numCourses)]
#         preq = {sub: [] for sub in range(numCourses)}
#         for i, j in prerequisites:
#             preq[i].append(j)
#         asker = set()
#         def dfs(subject, asker):
#             if can[subject] == True: return True
#             if preq[subject] == []: return True
#             if sub in asker and can[asker] == False: return False
            
#             for req in preq[subject]:
#                 asker.add(subject)
#                 can[sub] = dfs(req, asker)
                
#         for i in can:
#             if i == False:
#                 return False