from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        count = 0
        
        visited = set()
        temp_island = set()
        temp_subisland = set()
        
        rows, cols = len(grid2), len(grid2[0])
        
        def find_island_cells(grid, r, c, island):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r, c) in island:
                return
            
            island.add((r, c))
            
            find_island_cells(grid, r - 1, c, island)
            find_island_cells(grid, r + 1, c, island)
            find_island_cells(grid, r, c - 1, island)
            find_island_cells(grid, r, c + 1, island)
            
            return island
            
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid2[row][col] == 1 and grid1[row][col] == 1:
                    if (row, col) not in temp_island:
                        temp_island = find_island_cells(grid1, row, col, set())
                    
                    temp_subisland = find_island_cells(grid2, row, col, set())
                    
                    if temp_subisland <= temp_island:
                        count += 1
                    
                    visited |= temp_subisland
        
        return count
    
    
grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]

print(len(grid1))
solution = Solution()


print(solution.countSubIslands(grid1, grid2))

# A = {1, 2, 3}
# B = {1, 2, 3, 4, 5}

# if A <= B:
#     print("A is a subset of B")
# else:
#     print("A is NOT a subset of B")

