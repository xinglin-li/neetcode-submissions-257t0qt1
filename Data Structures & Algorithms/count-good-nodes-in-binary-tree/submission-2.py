# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(node, parent_val):
            if not node:
                return 0
            node_val = node.val
            max_val = max(node_val, parent_val)
            left = dfs(node.left, max_val)
            right = dfs(node.right, max_val)
            if node.val >= parent_val:
                return left + right + 1
            else:
                return left + right
        
        res = dfs(root, float("-inf"))
        return res