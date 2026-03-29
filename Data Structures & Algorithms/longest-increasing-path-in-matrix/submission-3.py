class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dfs + memoization, DP on DAG
        # An important conclusion: 
        # 1) DFS + memo is an universal solution for DP
        # 2) Not every DP can be written as bottom-up DP, you have to know the topological order
        # This is a question you have to use dfs + memo since you don't know topological order
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]  # memo

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]

            best = 1
            for dx, dy in dirs:
                x, y = i+dx, j+dy
                # The following matrix condition is the key
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    best = max(best, 1 + dfs(x, y))

            dp[i][j] = best
            return best

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i,j))

        return ans
