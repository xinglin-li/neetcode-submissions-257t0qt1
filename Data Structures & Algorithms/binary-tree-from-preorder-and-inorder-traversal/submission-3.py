# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {v:i for i,v in enumerate(inorder)}

        def build(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r:
                return
            root_val = preorder[pre_l]
            root = TreeNode(root_val)
            in_root_index = index[root_val]
            l_len = in_root_index - in_l

            root.left = build(pre_l + 1, pre_l + l_len, in_l, in_root_index - 1)
            root.right = build(pre_l + l_len + 1, pre_r, in_root_index + 1, in_r)
            return root
        return build(0, len(preorder)-1, 0, len(inorder)-1)