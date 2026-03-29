# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, path_max):
            if not node:
                return
            nonlocal count
            if node.val >= path_max:
                count += 1
                path_max = node.val
            dfs(node.left, path_max)
            dfs(node.right, path_max)
        
        dfs(root,float("-inf"))
        return count

            

