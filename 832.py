from typing import List

def flipAndInvertImage(image: List[List[int]]) -> List[List[int]]:
    n = len(image)
    for i in range(n):
        for j in range(n // 2):
            image[i][j], image[i][n - j - 1] = image[i][n - j - 1], image[i][j]
            image[i][j] ^= 1
            image[i][n - j - 1] ^= 1
        
        if n % 2 == 1:
            image[i][n // 2] ^= 1
        
    return image

image = [[1,1,0],[1,0,1],[0,0,0]]
print(flipAndInvertImage(image))
