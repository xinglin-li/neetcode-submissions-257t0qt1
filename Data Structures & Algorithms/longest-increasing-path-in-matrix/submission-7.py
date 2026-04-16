from functools import lru_cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        m, n = len(matrix), len(matrix[0])
        @lru_cache(None)
        def dfs(i,j):
            best = 1
            for dx, dy in dirs:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and matrix[i][j] < matrix[x][y]:
                    best = max(best, 1 + dfs(x,y))
            return best

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i,j))
        return ans
