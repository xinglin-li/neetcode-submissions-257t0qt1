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
        def dfs(r, c, size):
            if size == 1:
                return Node(val=(grid[r][c] == 1), isLeaf=True)
            
            half = size // 2

            tl = dfs(r, c, half)
            tr = dfs(r, c + half, half)
            bl = dfs(r + half, c, half)
            br = dfs(r + half, c + half, half)

            if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and (tl.val == tr.val == bl.val == br.val):
                return Node(val=tl.val, isLeaf=True)
            
            return Node(True, False, tl, tr, bl, br)
        
        return dfs(0, 0, len(grid))
