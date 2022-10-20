class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, des, cost in times:
            graph[src - 1].append([des - 1, cost])
        heap = [(0, k - 1)]        
        dist = [inf] * n
        dist[k - 1] = 0         
        visited = [False] * n
        while heap:
            _, node = heapq.heappop(heap)
            if visited[node]: continue
            visited[node] = True
            for neighbour, time in graph[node]:
                if dist[node] + time < dist[neighbour]:
                    dist[neighbour] = dist[node] + time                    
                    heapq.heappush(heap, [dist[neighbour], neighbour])
        ans = max(dist)
        return -1 if ans == inf else ans
        # graph = []
        # for src, dest, cost in times:
        #     graph.append([src - 1, dest - 1, cost])            
        # dist = [inf] * n
        # dist[k - 1] = 0             
        # def bellman_ford():
        #     for src, des, cost in graph:                
        #         if dist[src] != inf and dist[src] + cost < dist[des]:                 
        #             dist[des] = dist[src] + cost                
        # for _ in range(n - 1):
        #     bellman_ford()             
        # ans = max(dist)
        # return -1 if ans == inf else ans
            