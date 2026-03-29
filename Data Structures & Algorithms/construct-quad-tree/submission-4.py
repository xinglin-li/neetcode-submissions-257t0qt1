"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def dfs(r,c,size):
            same = True
            val = grid[r][c]
            for i in range(r, r+size):
                for j in range(c, c+size):
                    if grid[i][j] != val:
                        same = False
                        break
            if same:
                return Node(val==1, True, None, None, None, None)

            half = size//2
            TL = dfs(r,c,half)
            TR = dfs(r,c+half,half)
            BL = dfs(r+half,c,half)
            BR = dfs(r+half,c+half,half)
            return Node(val==1, False, TL, TR, BL, BR)
        return dfs(0,0,n)


                    
