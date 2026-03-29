# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while p.val < cur.val and q.val < cur.val:
            cur = cur.left

        while p.val > cur.val and q.val > cur.val:
            cur = cur.right
    
        return cur