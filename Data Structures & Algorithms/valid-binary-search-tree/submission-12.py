# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 方法一（最标准）：Range / Bounds DFS。如果是BST, 你就可以根据当前节点的值，以及左右子节点的值，确认左右子树的节点取值范围。
        def dfs(node, low, high):
            if not node:
                return True
            if not low < node.val < high:
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root, float("-inf"), float("inf"))
