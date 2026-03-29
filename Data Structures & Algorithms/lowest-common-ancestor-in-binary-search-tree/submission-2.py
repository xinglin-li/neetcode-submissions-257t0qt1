# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pv, qv = p.val, q.val
        cur = root
        while cur:
            if pv < cur.val and qv < cur.val:
                cur = cur.left
            elif pv > cur.val and qv > cur.val:
                cur = cur.right
            else:
                return cur   # split here, or cur is p/q