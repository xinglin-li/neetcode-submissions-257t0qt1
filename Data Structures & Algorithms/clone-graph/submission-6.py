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
        visited = {node: Node(node.val)}
        q = deque([node])

        while q:
            curr = q.popleft()
            for nei in curr.neighbors:
                if nei not in visited:
                    # 发现新节点，克隆并入队
                    q.append(nei)
                    visited[nei] = Node(nei.val)
                # 建立新图中的边连接
                visited[curr].neighbors.append(visited[nei])

        return visited[node]