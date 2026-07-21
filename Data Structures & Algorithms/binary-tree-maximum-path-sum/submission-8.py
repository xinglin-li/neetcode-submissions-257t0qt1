# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 初始化全局最大路径和为负无穷（处理树节点全为负数的极值情况）
        self.max_sum = float("-inf")

        def max_gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            # 1. 递归计算左右子树能提供的最大单边贡献，负数则直接舍弃（取 0）
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # 2. 假设当前节点是这条最大路径的“最高拐点”
            # 路径长度为：当前节点值 + 左分支最大贡献 + 右分支最大贡献
            price_newpath = node.val + left_gain + right_gain

            # 3. 用当前拐点的路径和更新全局最大值
            self.max_sum = max(self.max_sum, price_newpath)

            # 4. 向父节点返回当前节点能提供的最大单边贡献（只能选左右较长的一条）
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum