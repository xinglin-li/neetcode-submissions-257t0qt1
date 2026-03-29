"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(cur):
            if not cur:
                return None
            # 已经复制过，直接返回新节点
            if cur in old_to_new:
                return old_to_new[cur]
            
            # 1️⃣ 创建新节点（值相同）
            copy = Node(cur.val)
            old_to_new[cur] = copy

            # 2️⃣ 递归复制邻居
            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        return dfs(node)
