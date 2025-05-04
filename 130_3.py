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
            if (r, c) in non_surroundeds:
                return False
            
            if r == 0 or r == rows - 1 or c == 0 or c == cols -1:
                return False
            
            board[r][c] = "X"
            temp.add((r, c))
   
            if (board[r - 1][c] == "O" and not is_surrounded(r - 1, c)) or \
                (board[r + 1][c] == "O" and not is_surrounded(r + 1, c)) or \
                (board[r][c - 1] == "O" and not is_surrounded(r, c - 1)) or \
                (board[r][c + 1] == "O" and not is_surrounded(r, c + 1)):
                    return False
            
            return True
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and ((row, col)) not in non_surroundeds:
                    temp = set()
                    if not is_surrounded(row, col):
                        for (r, c) in temp:
                            board[r][c] = "O"
                            non_surroundeds.add((r, c))
                             
        return
                        

x = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]

solution = Solution()
solution.solve(x)

print(x)
