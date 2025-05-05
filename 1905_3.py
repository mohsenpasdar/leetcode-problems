from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        count = 0
                
        rows, cols = len(grid2), len(grid2[0])
        
        def dfs_check_subisland(r, c):
            subisland = True
            
            if r < 0 or r >= rows or c < 0 or c >= cols or grid2[r][c] != 1:
                return True
            
            grid2[r][c] = 0
            
            if subisland and grid1[r][c] == 0:
                subisland = False
            if not dfs_check_subisland(r - 1, c):
                subisland = False
            if not dfs_check_subisland(r + 1, c):
                subisland = False
            if not dfs_check_subisland(r, c - 1):
                subisland = False
            if not dfs_check_subisland(r, c + 1):
                subisland = False
            
            return subisland
        
        for row in range(rows):
            for col in range(cols):
                if grid2[row][col] == 1 and grid1[row][col] == 1:
                    if dfs_check_subisland(row, col):
                        count +=1
                    
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

