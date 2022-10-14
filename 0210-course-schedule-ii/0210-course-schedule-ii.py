class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        topo = []
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
        for c, _ in prerequisites:
            indegree[c] += 1
        q = deque()
        seen = set()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                seen.add(i)
        while q:
            a = q.popleft()
            topo.append(a)
            for node in graph[a]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.append(node)
                    seen.add(node)
        return topo if len(topo) == numCourses else []