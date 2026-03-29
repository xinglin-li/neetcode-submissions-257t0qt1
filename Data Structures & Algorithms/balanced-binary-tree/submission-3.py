# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.max_diff = 0
        def dfs(node):
            if not node:
                return 0
            dl = dfs(node.left)
            dr = dfs(node.right)
            self.max_diff = max(self.max_diff,abs(dl-dr))
            return 1 + max(dl, dr)
        dfs(root)
        return self.max_diff <= 1
        
