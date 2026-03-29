class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 这题（Valid Sudoku）的“标准答案”套路就是：一次遍历，用 3 组集合分别记录 行 / 列 / 3×3 宫已经出现过的数字，遇到重复就直接 False。
        # 关键点：3×3 宫的编号公式: box = (r//3)*3 + c//3
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # 0..8 表示 9 个 3x3 宫

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == '.':
                    continue

                b = (r // 3) * 3 + (c // 3)  # 宫编号：0..8

                if v in rows[r] or v in cols[c] or v in boxes[b]:
                    return False

                rows[r].add(v)
                cols[c].add(v)
                boxes[b].add(v)

        return True