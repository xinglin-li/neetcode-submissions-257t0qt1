# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            # 1. 一路向左压栈，直达当前子树的最左下角（最小值）
            while curr:
                stack.append(curr)
                curr = curr.left

            # 2. 弹出当前最小的节点
            curr = stack.pop()
            k -= 1

            # 3. 找到第 k 小的元素，提前终止并返回
            if k == 0:
                return curr.val

            # 4. 转向右子树
            curr = curr.right

        return -1