class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        non_surroundeds = set()
        
        rows = len(board)
        cols = len(board[0])
        
        def is_surrounded(r, c):
            temp.add((r, c))
            
            if (r, c) in non_surroundeds:
                return False
                
            if board[r - 1][c] == "O" and (r - 1, c) not in temp:
                if not is_surrounded(r - 1, c):
                    return False
            if board[r + 1][c] == "O" and (r + 1, c) not in temp:
                if not is_surrounded(r + 1, c):
                    return False
            if board[r][c - 1] == "O" and (r, c - 1) not in temp:
                if not is_surrounded(r, c - 1):
                    return False
            if board[r][c + 1] == "O" and (r, c + 1) not in temp:
                if not is_surrounded(r, c + 1):
                    return False
            
            return True
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                        non_surroundeds.add((row, col))
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and ((row, col)) not in non_surroundeds:
                    temp = set()
                    if is_surrounded(row, col):
                        for (r, c) in temp:
                            board[r][c] = "X"
                    else:
                        for (r, c) in temp:
                            non_surroundeds.add((r, c))
        
        return
                        

x = [["O","X","X","O","O"],
     ["X","O","O","X","O"],
     ["X","O","X","O","X"],
     ["O","X","O","O","O"],
     ["X","X","O","X","O"]]

[['O', 'x', 'O', 'O', 'X', 'X'], 
 ['O', 'O', 'O', 'O', 'O', 'O'], 
 ['O', 'X', 'O', 'X', 'O', 'O'], 
 ['O', 'X', 'O', 'O', 'X', 'O'], 
 ['O', 'X', 'O', 'X', 'O', 'O'], 
 ['O', 'X', 'O', 'O', 'O', 'O']]

# [['O', 'O', 'O', 'O', 'X', 'X'], 
#  ['O', 'O', 'O', 'O', 'O', 'O'], 
#  ['O', 'X', 'O', 'X', 'O', 'O'], 
#  ['O', 'X', 'O', 'X', 'X', 'O'], 
#  ['O', 'X', 'O', 'X', 'O', 'O'], 
#  ['O', 'X', 'O', 'O', 'O', 'O']]

solution = Solution()
solution.solve(x)

print(x)
