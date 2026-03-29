# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        l = root.left
        r = root.right
        if l or r:
            root.left = r
            root.right = l
        Solution.invertTree(self, root.left)
        Solution.invertTree(self, root.right)
        return root