# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 方法二（面试常见）：Inorder Traversal。BST 的一个重要性质：中序遍历（inorder）一定是严格递增的.
        prev = float("-inf")

        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            nonlocal prev
            if prev < node.val:
                prev = node.val
            else:
                return False
            return inorder(node.right)
        
        return inorder(root)