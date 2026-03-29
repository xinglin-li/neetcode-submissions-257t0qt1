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
        def build(r0, c0, length):
            first = grid[r0][c0]
            same = True 
            for i in range(r0, r0 + length):
                for j in range(c0, c0 + length):
                    if grid[i][j] != first:
                        same = False
                        break
                if not same:
                    break
            if same:
                return Node(first == 1, same, None, None, None, None)
            
            length = length//2
            node = Node(first == 1, same, 
            build(r0, c0, length),
            build(r0,c0 + length, length),
            build(r0+length,c0,length),
            build(r0+length,c0+length,length))
            return node
        n = len(grid)
        return build(0,0,n)