# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_idx = 0
        inorder_map = {v:i for i,v in enumerate(inorder)}
        def build_tree(l,r):
            if l>r:
                return None
            nonlocal pre_idx
            node = TreeNode(preorder[pre_idx])
            m = inorder_map[preorder[pre_idx]]
            pre_idx += 1
            node.left = build_tree(l,m-1)
            node.right = build_tree(m+1,r)
            return node
        return build_tree(0,len(preorder)-1)