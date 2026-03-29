class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n = len(matrix), len(matrix[0])
        matrix_trans = [[0]*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                matrix_trans[j][i] = matrix[i][j]
        return matrix_trans