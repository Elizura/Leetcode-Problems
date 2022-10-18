class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:                
        num = 1
        ans = [[0] * n for _ in range(n)]

        def spiral(left, right, top, bottom):
            nonlocal num
            if left == right == top == bottom:
                ans[right][left] = num
                return 
            #left to right (top one)
            for i in range(left, right + 1):
                ans[top][i] = num
                num += 1
            
            top += 1
            
            #top to bottom (right one)
            for i in range(top, bottom + 1):
                ans[i][right] = num
                num += 1
            right -= 1
            
            #right to left
            for i in range(right, left - 1, -1):
                ans[bottom][i] = num
                num += 1
            bottom -= 1
            
            #bottom to top
            for i in range(bottom, top - 1, -1):
                ans[i][left] = num
                num += 1
            
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        while left <= right and top <= bottom:          
            spiral(left, right, top, bottom)
            left += 1
            right -= 1
            top += 1
            bottom -= 1            
        return ans