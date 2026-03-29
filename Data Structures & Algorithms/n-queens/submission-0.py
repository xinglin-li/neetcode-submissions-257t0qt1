class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # A key is that you notice the relationship between c and r in diagonal
        res = []
        board = [['.']*n for _ in range(n)]
        col_set = set()
        diag_1 = set()
        diag_2 = set()

        def backtrack(r):
            if r == n:
                res.append([''.join(c) for c in board])
                return 

            for c in range(n):
                if c in col_set or r - c in diag_1 or r + c in diag_2:
                    continue
                board[c][r] = 'Q'
                col_set.add(c)
                diag_1.add(r-c)
                diag_2.add(r+c)
                backtrack(r+1)
                board[c][r] = '.'
                col_set.remove(c)
                diag_1.remove(r-c)
                diag_2.remove(r+c)
        
        backtrack(0)
        return res



