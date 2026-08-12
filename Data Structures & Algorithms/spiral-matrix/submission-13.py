class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        # 定义当前的四个边界范围
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        res = []

        while top <= bottom and left <= right:
            # 1. 从左到右遍历上边界
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1 # 缩小上边界
            # 2. 从上到下遍历右边界
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1 # 缩小右边界
            # 3. 从右到左遍历下边界 (需确保当前还存在未遍历的行)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1
            # 4. 从下到上遍历左边界（需确保当前还存在未遍历的列）
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1  # 缩小左边界
            
        return res