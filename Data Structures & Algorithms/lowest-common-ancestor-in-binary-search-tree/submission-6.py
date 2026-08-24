# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            # 两个节点都在右子树
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # 两个节点都在左子树
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # 分岔点即为最近公共祖先
            else:
                return curr
        return None