class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
            
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        # 反向思维：从大洋边界逆流向内陆 DFS（高度只能相等或更高）
        def dfs(r, c, visited, prev_height):
            if ((r, c) in visited or 
                r < 0 or c < 0 or r >= rows or c >= cols or 
                heights[r][c] < prev_height):
                return
            
            visited.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(r + dr, c + dc, visited, heights[r][c])
                
        # 1. 太平洋边界（顶部行与左侧列）/ 大西洋边界（底部行与右侧列）
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])                # 太平洋顶边
            dfs(rows - 1, c, atlantic, heights[rows - 1][c]) # 大西洋底边
            
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])                # 太平洋左边
            dfs(r, cols - 1, atlantic, heights[r][cols - 1]) # 大西洋右边
            
        # 2. 两个集合的交集即为既能流向太平洋又能流向大西洋的坐标
        return list(pacific & atlantic)
        