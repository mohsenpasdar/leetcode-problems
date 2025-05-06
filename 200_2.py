class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        
        rows, cols = len(grid), len(grid[0])
        
        def helper(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1": 
                return
            
            grid[r][c] = "0"
            
            helper(r - 1, c)
            helper(r + 1, c)
            helper(r, c - 1) 
            helper(r, c + 1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    helper(row, col)
                    count += 1
                    
        return count
        
solution = Solution()
print(solution.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
