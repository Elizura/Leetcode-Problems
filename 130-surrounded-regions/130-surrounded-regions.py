class Solution:
    def solve(self, board: List[List[str]]) -> None:
        a = lambda row: 0 <= row < len(board)
        b = lambda col: 0 <= col < len(board[0])
        seen = set()
        def dfs (row, col):
            if not a(row) or not b(col) or board[row][col] == "X" or (row, col) in seen:
                return
            seen.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            
        
        
        
        for col in range(len(board[0])):
            if board[0][col] == "O":
                dfs(0, col)
            if board[len(board) - 1][col] == "O":
                dfs(len(board) - 1, col)
        for row in range(len(board)):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][len(board[0]) - 1] == "O":
                dfs(row, len(board[0]) - 1)
                
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) not in seen:
                    board[row][col] = "X"
        """
        Do not return anything, modify board in-place instead.
        """
        