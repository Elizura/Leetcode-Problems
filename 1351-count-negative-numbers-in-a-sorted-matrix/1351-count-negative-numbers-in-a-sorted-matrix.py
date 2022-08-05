class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:     
        ans = 0
        row, column = len(grid) - 1, 0
        while row >= 0 and column < len(grid[0]):
            if grid[row][column] < 0:
                ans += len(grid[0]) - column
                row -= 1
            else:
                column += 1
        return ans
                
                