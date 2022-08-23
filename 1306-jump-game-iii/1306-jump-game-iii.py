class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        N = len(arr)
        inrange = lambda s: 0 <= s < N        
        q = deque()        
        q.append(start)
        seen = set()
        seen.add(start)
        found = False
        while not found and q:            
            a = q.popleft()
            # seen.add(a)
            if arr[a] == 0: found = True            
            if inrange(a + arr[a]) and (a + arr[a]) not in seen:
                q.append(a + arr[a])  
                seen.add(a + arr[a])
            if inrange(a - arr[a]) and (a - arr[a]) not in seen:
                q.append(a - arr[a])
                seen.add(a - arr[a])
        return found
            
            
        