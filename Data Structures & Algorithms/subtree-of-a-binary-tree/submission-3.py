# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root:
            return False

        def isSame(root, node):
            if not root and not node:
                return True
            if not root or not node:
                return False
            if root.val != node.val:
                return False
            return isSame(root.left, node.left) and isSame(root.right, node.right)
        
        return isSame(root,subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
