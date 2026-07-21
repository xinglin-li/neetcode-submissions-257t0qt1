# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = []

        def dfs(node):
            if not node:
                serialized.append("N")
                return
            serialized.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(serialized)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i = 0
        values = data.split(",")
        def dfs():
            nonlocal i
            if i == len(values):
                return None
            if values[i] == "N":
                i += 1
                return None
            node = TreeNode(int(values[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        root = dfs()
        return root

