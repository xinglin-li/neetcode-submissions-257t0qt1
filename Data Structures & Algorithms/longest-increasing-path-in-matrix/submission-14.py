class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 记忆化 DFS（DAG 上的最长路径）。由于路径必须严格递增，矩阵天然无环，各位置的最长路径相互独立且固定。
        from functools import cache
        m, n = len(matrix), len(matrix[0])

        @cache
        def dfs(r, c):
            res = 1
            for dr, dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, 1 + dfs(nr, nc))
            return res
        
        return max(dfs(r, c) for r in range(m) for c in range(n))