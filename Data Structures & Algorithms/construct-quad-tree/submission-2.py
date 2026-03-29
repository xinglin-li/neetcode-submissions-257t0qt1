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
            # 检查区域是否一致
            first = grid[r0][c0]
            same = True
            for i in range(r0, r0 + length):
                for j in range(c0, c0 + length):
                    if grid[i][j] != first:
                        same = False
                        break
                if not same:
                    break

            # 如果全一样：叶子节点
            if same:
                return Node(first == 1, True, None, None, None, None)

            # 否则拆成 4 块
            half = length // 2
            return Node(
                True,  # val 任意写（题目说 isLeaf=False 时 val 可随便）
                False,
                build(r0, c0, half),                    # topLeft
                build(r0, c0 + half, half),             # topRight
                build(r0 + half, c0, half),             # bottomLeft
                build(r0 + half, c0 + half, half)       # bottomRight
            )

        n = len(grid)
        return build(0, 0, n)