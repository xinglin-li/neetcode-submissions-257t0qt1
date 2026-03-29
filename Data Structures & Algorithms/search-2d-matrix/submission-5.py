class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1
        while l <= r:
            mid = (l+r)//2
            col = mid//n
            row = mid%n
            if matrix[col][row] == target:
                return True
            elif matrix[col][row] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
