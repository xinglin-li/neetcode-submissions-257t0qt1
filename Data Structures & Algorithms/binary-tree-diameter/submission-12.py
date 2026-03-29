# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def dfs(node):
            if not node:
                return 0
            self.diameter = max(self.diameter, dfs(node.left) + dfs(node.right))
            return 1 + max(dfs(node.left), dfs(node.right))
        dfs(root)
        return self.diameter