class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:   
        seen = set()
        def invalid(row, col, par, s):            
            if row < 0 or row >= len(grid): return True            
            if col < 0 or col >= len(grid[0]): return True                        
            a, b = s
            if grid[row][col] != grid[a][b]: return True
            if (row, col) == par: return True
        def cycle(row, col, par):               
            if (row, col) in seen: return True
            seen.add((row, col))
            d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for r, c in d:
                if not invalid(row + r, col + c, par, (row, col)):
                    if cycle(row + r, col + c, (row, col)):
                        return True
            return False
            
        row, col = len(grid), len(grid[0])
        for r in range(row):
            for c in range(col):
                if (r, c) not in seen:                                                     
                    if cycle(r, c, (inf, inf)):
                        return True
        return False