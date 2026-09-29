# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, prev_max):
            if not node:
                return
            nonlocal count
            if prev_max <= node.val:
                count += 1
            prev_max = max(prev_max, node.val)
            dfs(node.left, prev_max)
            dfs(node.right, prev_max)
        
        dfs(root, float("-inf"))
        return count


