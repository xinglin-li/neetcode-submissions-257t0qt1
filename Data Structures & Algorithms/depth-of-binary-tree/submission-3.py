# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # 分治：获取左右子树最大深度，取最大值加 1
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))