class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        islands = 0
        visited_set = set()
        
        rows = len(grid)
        cols = len(grid[0])
        
        def backtrack(i, j):
            if i > 0 and grid[i - 1][j] == "1" and (i - 1, j) not in visited_set:
                visited_set.add((i - 1, j))
                backtrack(i - 1, j)
            
            if i < rows - 1 and grid[i + 1][j] == "1" and (i + 1, j) not in visited_set:
                visited_set.add((i + 1, j))
                backtrack(i + 1, j)
                
            if j > 0 and grid[i][j - 1] == "1" and (i, j - 1) not in visited_set:
                visited_set.add((i, j - 1))
                backtrack(i, j - 1)
                
            if j < cols - 1 and grid[i][j + 1] == "1" and (i, j + 1) not in visited_set:
                visited_set.add((i, j + 1))
                backtrack(i, j + 1)
                
            return
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited_set:
                    visited_set.add((row, col))
                    backtrack(row, col)
                    islands += 1
                    
        return islands
        
solution = Solution()
print(solution.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
