# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node, key):
            if not node:
                return 

            if node.val == key:
                if not node.left and not node.right:
                    return None
                if not node.right:
                    return node.left
                if not node.left:
                    return node.right
                else:
                    successor = node.right
                    while successor.left:
                        successor = successor.left
                    node.val = successor.val
                    node.right = dfs(node.right,node.val)     
            if key < node.val:
               node.left = dfs(node.left, key)
            else:
               node.right= dfs(node.right, key)
            return node
        return dfs(root,key)
