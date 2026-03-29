# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float("-inf")

        def dfs(node) -> int:
            if not node:
                return 0
            left_gain = max(0, dfs(node.left))   # discard negative branches
            right_gain = max(0, dfs(node.right))
            # best path that *passes through* this node (could be final answer)
            self.best = max(self.best, node.val + left_gain + right_gain)
            # gain to propagate upward (must choose one side or none)
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.best