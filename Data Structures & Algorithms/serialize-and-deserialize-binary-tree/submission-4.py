# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Note: pre-order and post-order can recover. In-order cannot, since different trees can have the same in-order traverse results
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                return "null"
            left = dfs(node.left)
            right = dfs(node.right)
            return f"{node.val},{left},{right}"
        return dfs(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = iter(data.split(","))
        def dfs():
            val =  next(values)
            if val == "null":
                return None
            node = TreeNode(val)
            node.left = dfs()
            node.right= dfs()
            return node
        return dfs()

