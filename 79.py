class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited_set = set()
        
        rows, cols = len(board), len(board[0])
        
        def search(i, j, idx):
            visited_set.add((i, j))
            
            if idx == len(word):
                return True
            
            if i > 0 and board[i - 1][j] == word[idx] and (i - 1, j) not in visited_set:
                if search(i - 1, j, idx + 1):
                    return True
            
            if i < rows - 1 and board[i + 1][j] == word[idx] and (i + 1, j) not in visited_set:
                if search(i + 1, j, idx + 1):
                    return True
            
            if j > 0 and board[i][j - 1] == word[idx] and (i, j - 1) not in visited_set:
                if search(i, j - 1, idx + 1):
                    return True
            
            if j < cols - 1 and board[i][j + 1] == word[idx] and (i, j + 1) not in visited_set:
                if search(i, j + 1, idx + 1):
                    return True
            
            visited_set.remove((i, j))
            return False
            
        
        
        for row in range(rows):
            for col in range(cols):
                if word[0] == board[row][col]:
                    if search(row, col, 1):
                        return True
                    
        return False
        
    
        
            
        
        
solution = Solution()
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ASAD"))

# a = [1, 2, 3]
# print(a[3:])