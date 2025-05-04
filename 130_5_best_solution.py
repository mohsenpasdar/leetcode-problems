class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
                
        rows, cols = len(board), len(board[0])
        
        def overwrite(r, c):          
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return
            
            board[r][c] = "T"

            overwrite(r - 1, c)
            overwrite(r + 1, c)
            overwrite(r, c - 1)
            overwrite(r, c + 1)
            
        for col in range(cols):
            if board[0][col] == "O":
                overwrite(0, col)
            if board[rows - 1][col] == "O":
                overwrite(rows - 1, col)
        
        for row in range(rows):
            if board[row][0] == "O":
                overwrite(row, 0)
            if board[row][cols - 1] == "O":
                overwrite(row, cols - 1)
                
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "T":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"
                             
        return
                        

x = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]

solution = Solution()
solution.solve(x)

print(x)
