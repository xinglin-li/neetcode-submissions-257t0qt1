# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        node = root
        while True:
            if node.val > val:
                if node.left:
                    node = node.left
                    continue
                node.left = TreeNode(val)
                break
            else:
                if node.right:
                    node = node.right
                    continue
                node.right = TreeNode(val)
                break
        return root

