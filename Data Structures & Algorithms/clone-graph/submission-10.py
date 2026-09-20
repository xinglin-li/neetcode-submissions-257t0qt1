"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_to_new = {}

        def dfs(curr):
            if curr in old_to_new:
                return old_to_new[curr]
            
            clone = Node(curr.val)
            old_to_new[curr] = clone

            for nei in curr.neighbors:
                clone.neighbors.append(dfs(nei))
            
            return clone
        return dfs(node)