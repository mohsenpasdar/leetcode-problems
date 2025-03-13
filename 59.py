from typing import List

def generateMatrix(n: int) -> List[List[int]]:
        array = [[None] * n for _ in range(n)]
        temp = 1
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                array[i][j] = temp
                temp += 1
            
            for k in range(i, n - i - 1):
                array[k][n - 1 -i] = temp
                temp += 1

            for l in range(n - i - 1, i, -1):
                array[ n - 1 - i][l] = temp
                temp += 1
            
            for m in range(n - i - 1, i, -1):
                array[m][i] = temp
                temp += 1
            
        if n % 2 == 1: array[n // 2][n // 2] = n ** 2
        return array

print(generateMatrix(3))