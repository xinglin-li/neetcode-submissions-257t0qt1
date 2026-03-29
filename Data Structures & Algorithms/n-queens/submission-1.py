class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # A key is that you notice the relationship between c and r in diagonal
        res = []
        board = [["."] * n for _ in range(n)]

        cols = set()          # 放过皇后的列
        diag1 = set()         # r - c 斜线
        diag2 = set()         # r + c 斜线

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue

                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                board[r][c] = "Q"

                backtrack(r + 1)

                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)
                board[r][c] = "."

        backtrack(0)
        return res



