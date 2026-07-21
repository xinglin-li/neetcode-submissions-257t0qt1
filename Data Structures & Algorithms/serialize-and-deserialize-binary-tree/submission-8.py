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
        # 修复 1：使用逗号作为分隔符
        return ",".join(serialized)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # 修复 2：先按逗号切分成字符串列表
        vals = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            if i == len(vals):
                return None
            if vals[i] == "N":
                i += 1
                return None

            # 修复 3：读取完整的数字 Token 并转化为 int
            node = TreeNode(int(vals[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

