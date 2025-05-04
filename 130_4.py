class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """        
        rows = len(board)
        cols = len(board[0])
        
        def is_surrounded(r, c):         
            if r == 0 or r == rows - 1 or c == 0 or c == cols -1:
                return False
            
            board[r][c] = "T"
   
            if (board[r - 1][c] == "O" and not is_surrounded(r - 1, c)) or \
                (board[r + 1][c] == "O" and not is_surrounded(r + 1, c)) or \
                (board[r][c - 1] == "O" and not is_surrounded(r, c - 1)) or \
                (board[r][c + 1] == "O" and not is_surrounded(r, c + 1)):
                    return False
            
            return True
        
        def change(r, c, stri):
            if board[r][c] == "T":          
                board[r][c] = stri
                change(r - 1, c, stri)
                change(r + 1, c, stri)
                change(r, c - 1, stri)
                change(r, c + 1, stri)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    if is_surrounded(row, col):
                        change(row, col, "X")
                    else:
                        change(row, col, "O")
                          
        return
          
# x = [["X","X","X","X"],
#      ["X","O","O","O"],
#      ["X","O","X","X"],
#      ["X","X","X","X"]]              

x = [
 ["O","O","O","O","X","X"],
 ["O","O","O","O","O","O"],
 ["O","X","O","X","O","O"],
 ["O","X","O","O","X","O"],
 ["O","X","O","X","O","O"],
 ["O","X","O","O","O","O"]]

# [['O', 'O', 'O', 'O', 'X', 'X'], 
#  ['O', 'O', 'O', 'O', 'O', 'O'], 
#  ['O', 'X', 'O', 'X', 'O', 'O'], 
#  ['O', 'X', 'O', 'O', 'X', 'O'], 
#  ['O', 'X', 'O', 'X', 'O', 'O'], 
#  ['O', 'X', 'O', 'O', 'O', 'O']]

solution = Solution()
solution.solve(x)

print(x)
