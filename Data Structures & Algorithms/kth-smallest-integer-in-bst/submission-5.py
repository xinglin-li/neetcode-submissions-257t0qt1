# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # the kth number of inorder traverse
        res = 0
        order = 1
        def dfs(node):
            nonlocal order
            if not node:
                return
            if order > k:
                return 
            dfs(node.left)
            nonlocal res
            if order == k:
                res = node.val
            order += 1
            dfs(node.right)
        dfs(root)
        return res