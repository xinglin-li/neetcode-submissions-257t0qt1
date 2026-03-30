"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        # 记录已经访问过的节点，字典的键是原始节点，值是克隆节点
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        # 如果该节点已经被克隆过，直接从哈希表中返回，避免死循环
        if node in self.visited:
            return self.visited[node]

        # 1. 创建当前节点的克隆节点（此时邻居列表为空）
        clone_node = Node(node.val, [])

        # 2. 将新创建的克隆节点存入哈希表
        self.visited[node] = clone_node

        # 3. 递归遍历原节点的所有邻居，并将克隆后的邻居追加到克隆节点的邻居列表中
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node
        