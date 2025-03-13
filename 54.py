from typing import List
import math


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    result = []
    return helper(result, matrix)

def helper(array: List[int], matrix: List[List[int]]) -> List[int]:
    m = len(matrix)
    if m == 0:
        return array
    
    if m == 1:
        array.extend(matrix[0])
        return array
    
    n = len(matrix[0])
    if n == 0:
        return array

    if n == 1:
            array.extend([row[0] for row in matrix])
            return array

    for j in range(0, n - 1):
        array.append(matrix[0][j])
    
    for k in range(0, m - 1):
        array.append(matrix[k][n - 1])
        
    for l in range(n - 1, 0, -1):
        array.append(matrix[m - 1][l])
        
    for h in range(m - 1, 0, -1):
        array.append(matrix[h][0])
    
    newMatrix = [row[1:-1] for row in matrix[1:-1]]
            
    return helper(array, newMatrix)


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]
print(spiralOrder(matrix))

print(len([]))