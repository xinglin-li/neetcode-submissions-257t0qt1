# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 哈希表快速查找 inorder 中根节点的值对应下标
        in_map = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None
            # 前序区间的首节点为根
            root_val = preorder[pre_left]
            root = TreeNode(root_val)     
            # 在中序序列中切分左右子树
            in_root_idx = in_map[root_val]
            left_size = in_root_idx - in_left  # 左子树节点总数           
            # 递归构建左右子树
            root.left = helper(pre_left + 1, pre_left + left_size, in_left, in_root_idx - 1)
            root.right = helper(pre_left + left_size + 1, pre_right, in_root_idx + 1, in_right)         
            return root
            
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)