class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r,c, visited, height):
            if r < 0 or r > m - 1 or c < 0 or c > n -1 or heights[r][c] < height or (r,c) in visited:
                return
            visited.add((r,c))
            dfs(r+1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
        
        for c in range(n):
            dfs(0, c, pacific, heights[0][c])
            dfs(m-1, c, atlantic, heights[m-1][c])
        
        for r in range(m):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, n-1, atlantic, heights[r][n-1])
        
        return list(pacific&atlantic)
        