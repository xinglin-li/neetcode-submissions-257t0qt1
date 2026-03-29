# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Using DFS
        if not root:
            return []
        ans = []
        def dfs(node, depth):
            if not node:
                return
            if depth == len(ans):
                ans.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root,0)
        return ans

"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Using bfs. Note that the last node in each level is the node of right side view.
        if not root:
            return []
        q = [root]
        ans = []

        while q:
            level_size = len(q)
            for i in range(level_size):
                node = q.pop(0)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                if i == level_size - 1:   # 这一层最后一个
                    ans.append(node.val)
        return ans
"""
