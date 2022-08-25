class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        is_onborder_row = lambda row: row == 0 or row == len(maze) - 1
        is_onborder_col = lambda col: col == 0 or col == len(maze[0]) - 1
        inrangerow = lambda row: 0 <= row < len(maze)
        inrangecol = lambda col: 0 <= col < len(maze[0])
        direc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ans = 0
        q = deque()
        q.append((entrance[0], entrance[1]))
        seen = set()
        while q:            
            for i in range(len(q)):
                row, col = q.popleft()                
                for j in direc:
                    a, b = row + j[0], col + j[1]
                    if not inrangerow(a) or not inrangecol(b) or (a, b) in seen: continue
                    if maze[a][b] == "." and inrangerow(a) and inrangecol(b):
                        if is_onborder_row(a) or is_onborder_col(b):
                            if entrance[0] != a or entrance[1] != b:
                                return ans + 1
                        seen.add((a, b))
                        q.append((a, b))                        
            ans += 1
        return -1
                
            
            
        