class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True
        dic = {i: [] for i in range (n)}
        for i in edges:
            dic[i[0]].append(i[1])
            dic[i[1]].append(i[0])
        q = deque([source])
        seen = set()
        while q:
            a = q.popleft()
            if a == destination:
                return True
            for i in dic[a]:
                if i not in seen:
                    q.append(i)
            seen.add(a)
        return False
        
        