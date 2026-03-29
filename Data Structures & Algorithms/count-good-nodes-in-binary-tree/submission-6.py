# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            good = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)
            return good + dfs(node.left, new_max) + dfs(node.right, new_max)
        return dfs(root, root.val)

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root,root.val)]
        ans = 0
        while stack:
            node, max_so_far = stack.pop()
            if node.val >= max_so_far:
                ans += 1
            new_max = max(node.val, max_so_far)
            if node.left:
                stack.append((node.left, new_max))
            if node.right:
                stack.append((node.right, new_max))
        return ans


"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(node, parent_val):
            if not node:
                return 0
            node_val = node.val
            max_val = max(node_val, parent_val)
            left = dfs(node.left, max_val)
            right = dfs(node.right, max_val)
            if node.val >= parent_val:
                return left + right + 1
            else:
                return left + right
        
        res = dfs(root, float("-inf")) # or dfs(root, root.val)
        return res
"""