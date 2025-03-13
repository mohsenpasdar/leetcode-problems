from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for i in range(0, n // 2):
        for j in range(i, n - i - 1):
            matrix[i][j], matrix[j][n - i - 1] = matrix[j][n - i - 1], matrix[i][j]
            matrix[i][j], matrix[n - i - 1][n - j - 1] = matrix[n - i - 1][n - j - 1], matrix[i][j]
            matrix[i][j], matrix[n - j - 1][i] = matrix[n - j - 1][i], matrix[i][j]


A = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(A)
rotate(A)
print(A)
# print(A[0][0])
# A[0][0], A[1][1] = A[1][1], A[0][0]
# print(A[0][0])
# print(A[1][1])

                