# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Using bfs. Note that the last node in each level is the node of right side view.
        if not root:
            return []
        q = [root]
        ans = [root.val]
        while q:
            level_size = len(q)
            for level in range(level_size):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if q:
                ans.append(q[-1].val)
        return ans
