class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        zero_i = set()
        zero_j = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_i.add(i)
                    zero_j.add(j)
        
        for i in zero_i:
            for j in range(n):
                matrix[i][j] = 0
        for i in range(m):
            for j in zero_j:
                matrix[i][j] = 0

        