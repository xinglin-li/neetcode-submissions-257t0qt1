class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m, n = len(grid), len(grid[0])
        # Use a set for 'visited' to track cells efficiently, 
        # or just modify the grid in-place (change 1s to 0s after visiting)

        def dfs(i, j):
            # Base cases: out of bounds, water (0), or already visited
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            
            # Mark the cell as visited by changing it to 0
            grid[i][j] = 0
            
            # Start the area count for this call at 1 (for the current cell)
            area = 1
            
            # Recursively call DFS for valid horizontal and vertical neighbors
            # and add their returned areas to the current area count
            area += dfs(i + 1, j) # Down
            area += dfs(i - 1, j) # Up
            area += dfs(i, j + 1) # Right
            area += dfs(i, j - 1) # Left
            
            return area

        # Iterate through every cell
        for i in range(m):
            for j in range(n):
                # If we find land (1), start a DFS to calculate that island's total area
                if grid[i][j] == 1:
                    current_island_area = dfs(i, j)
                    max_area = max(max_area, current_island_area)
        
        return max_area
