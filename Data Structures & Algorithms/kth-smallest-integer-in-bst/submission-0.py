# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def mid_traverse(node):
            if not node:
                return []
            res_l = mid_traverse(node.left)
            z = node.val
            res_r = mid_traverse(node.right)
            return res_l + [z] + res_r
        return mid_traverse(root)[k-1]
            