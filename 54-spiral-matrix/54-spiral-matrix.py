class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        left, top = 0, 0
        right = col - 1 
        bottom = row - 1
        
        output = []
        while len(output) < row * col:
            for r in range(left, right + 1):
                output.append(matrix[top][r])
            
            for b in range(top+1, bottom + 1):
                output.append(matrix[b][right])
            
            if top != bottom:
                for l in range(right-1, left-1, -1):
                    output.append(matrix[bottom][l])
            if left != right:
                for u in range(bottom-1, top, -1):
                    output.append(matrix[u][left])

            top += 1
            right -= 1
            bottom -= 1
            left += 1
            
    
            
        return output