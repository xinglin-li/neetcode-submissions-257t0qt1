class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # sophiscated 4 way rotation ring
        n = len(matrix)
        for layer in range(n // 2):
            first, last = layer, n - 1 - layer
            for j in range(first, last):
                offset = j - first
                top = matrix[first][j]                           # save top
                matrix[first][j] = matrix[last - offset][first]  # left -> top
                matrix[last - offset][first] = matrix[last][last - offset]  # bottom -> left
                matrix[last][last - offset] = matrix[j][last]    # right -> bottom
                matrix[j][last] = top                            # top -> right

"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # method 1: transpose then reverse row
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j],  matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:
            row.reverse()
"""