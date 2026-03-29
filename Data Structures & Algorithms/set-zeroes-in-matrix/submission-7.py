class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        r0 = any(matrix[0][j] == 0 for j in range(n))
        c0 = any(matrix[i][0] == 0 for i in range(m))

        # 1) 内部打标记：遇到 0 -> 该行首/该列首置 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 2) 按标记清零内部
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # 3) 处理首行/首列
        if r0:
            for j in range(n):
                matrix[0][j] = 0
        if c0:
            for i in range(m):
                matrix[i][0] = 0


"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #brute force solution
        #O(mn), O(m+n)
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
"""

        