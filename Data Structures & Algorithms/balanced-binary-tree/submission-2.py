# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0   # height = 0

            left = dfs(node.left)
            if left == -1:        # left subtree not balanced
                return -1

            right = dfs(node.right)
            if right == -1:       # right subtree not balanced
                return -1

            if abs(left - right) > 1:
                return -1         # current node not balanced

            return 1 + max(left, right)

        return dfs(root) != -1
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.diff = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.diff = max(self.diff,abs(left-right))
            return 1 + max(left,right)

        dfs(root)
        return False if self.diff > 1 else True
"""