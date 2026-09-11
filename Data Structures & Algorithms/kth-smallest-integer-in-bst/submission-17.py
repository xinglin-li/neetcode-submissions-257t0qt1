# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            if not node:
                return None    
            # 1. 搜寻左子树
            left = dfs(node.left)
            if left is not None:
                return left    
            # 2. 处理当前节点
            count += 1
            if count == k:
                return node.val       
            # 3. 搜寻右子树
            return dfs(node.right)

        return dfs(root)