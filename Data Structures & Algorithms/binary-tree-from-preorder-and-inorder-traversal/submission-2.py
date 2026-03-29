# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in inorder for O(1) splits
        pos = {v: i for i, v in enumerate(inorder)}
        pre_i = 0  # pointer on preorder

        def build(l: int, r: int) -> Optional[TreeNode]:
            nonlocal pre_i
            if l > r:
                return None
            root_val = preorder[pre_i]
            pre_i += 1
            m = pos[root_val]      # root position in inorder
            root = TreeNode(root_val)
            root.left  = build(l, m - 1)  # build left subtree
            root.right = build(m + 1, r)  # build right subtree
            return root

        return build(0, len(inorder) - 1)