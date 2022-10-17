class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:        
        q = deque([0])
        seen = set()
        while q:
            a = q.popleft()
            seen.add(a)
            for n in rooms[a]:
                if n not in seen:
                    q.append(n)
        return len(seen) == len(rooms)
        
        # def dfs(node):
        #     if node in seen: return 
        #     seen.add(node)
        #     for i in rooms[node]:
        #         dfs(i)
        # seen = set()
        # dfs(0)
        # return len(seen) == len(rooms)
#         graph = defaultdict(int)
#         for i in range(len(rooms)):
#             graph[i] = rooms[i]
#         seen = set()
#         def dfs(node):
#             if node in seen: return 
#             seen.add(node)
#             for i in graph[node]:
#                 if i not in seen:
#                     dfs(i)
                        
#         dfs(0)
#         return len(seen) == len(rooms)