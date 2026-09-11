# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder -> root left right
        # inorder -> left root right
        inorder_map = {val:i for i, val in enumerate(inorder)}
        def builder(left_pre, right_pre, left_in, right_in):
            if left_pre > right_pre:
                return None
            root_val = preorder[left_pre]
            inorder_root_idx = inorder_map[root_val]
            left_tree_len = inorder_root_idx - left_in
            right_tree_len = right_in - inorder_root_idx
            left = builder(left_pre + 1, left_pre + left_tree_len, left_in, inorder_root_idx -1)
            right = builder(left_pre + left_tree_len + 1, right_pre, inorder_root_idx + 1, right_in)
            node = TreeNode(root_val, left, right)
            return node
        return builder(0, len(preorder) -1, 0, len(inorder)-1)
