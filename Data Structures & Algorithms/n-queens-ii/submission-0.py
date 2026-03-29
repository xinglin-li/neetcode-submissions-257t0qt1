class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        cols = set()
        diag1 = set()
        diag2 = set()

        def dfs(r):
            nonlocal res
            if r == n:
                res += 1
                return
            for col in range(n):
                if col not in cols and r - col not in diag1 and r + col not in diag2:
                    cols.add(col)
                    diag1.add(r - col)
                    diag2.add(r + col)
                    dfs(r+1)
                    cols.remove(col)
                    diag1.remove(r - col)
                    diag2.remove(r + col)
                else:
                   continue 
            return
        dfs(0)
        return res