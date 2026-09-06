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
        
        # 原node -> clone node, 还能当做访问标记
        old_to_new = {}

        def dfs(curr):
            if curr in old_to_new:
                return old_to_new[curr]
            
            # 创建克隆节点
            clone = Node(curr.val)
            old_to_new[curr] = clone
            # 递归克隆所有邻居并加入邻居列表
            for nei in curr.neighbors:
                clone.neighbors.append(dfs(nei))
            
            return clone

        return dfs(node)
