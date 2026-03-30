class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 逆向思维 + DFS
        if not board:
            return
        
        m,n = len(board), len(board[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        def dfs(r,c):
            if r < 0 or r > m -1 or c < 0 or c > n-1 or board[r][c] != "O":
                return 
            board[r][c] = "#"
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                dfs(nr,nc)
        
        for r in range(m):
            dfs(r,0)
            dfs(r,n-1)
        for c in range(1,n-1):
            dfs(0,c)
            dfs(m-1,c)
        for r in range(m):
            for c in range(n):
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
