# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
            
        # 递归翻转左右子树
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        # 交换当前节点的左右子节点
        root.left, root.right = right, left
        
        return root