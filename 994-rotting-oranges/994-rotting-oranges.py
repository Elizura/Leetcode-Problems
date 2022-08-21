class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        minutes = 0        
        a = lambda row: 0 <= row < len(grid)
        b = lambda col: 0 <= col < len(grid[0])
        q = deque()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row, col))
                    
        while q and fresh:                              
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:                        
                    row, col = dr + r, dc + c
                    if not a(row) or not b(col): continue
                    if grid[row][col] != 1: continue
                    grid[row][col] = 2
                    fresh -= 1
                    q.append((row, col))                
            minutes += 1
        return -1 if fresh > 0 else minutes
            
                     
                     
                     
        # a = lambda row: 0 <= row < len(grid)
        # b = lambda col: 0 <= col < len(grid[0])
        # ans = [0]
        # def dfs(row, col):
        #     if not a(row) or not b(col) or grid[row][col] == 0: return
        #     if grid[row][col] == 1:
        #         grid[row][col] == 2
        #     dfs(row + 1, col)
        #     dfs(row - 1, col)
        #     dfs(row, col + 1)
        #     dfs(row, col - 1)
        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         if grid[row][col] == 2:
        #             dfs(row, col)
        