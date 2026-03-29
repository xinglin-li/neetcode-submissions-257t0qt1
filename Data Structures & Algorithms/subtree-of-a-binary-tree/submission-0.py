# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return not subRoot

        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        else:
            return self._same(root, subRoot)

    def _same(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot or root.val!=subRoot.val:
            return False
        return self._same(root.left, subRoot.left) and self._same(root.right, subRoot.right)