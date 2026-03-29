class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(r,c,i):
            if c < 0 or c > n - 1 or r < 0 or r > m - 1 or board[r][c] != word[i]:
                return False
            if i + 1 == len(word):
                return True
            
            temp = board[r][c]
            board[r][c] = "#"
            found = (
                dfs(r-1,c,i+1) or
                dfs(r+1,c,i+1) or
                dfs(r,c-1,i+1) or
                dfs(r,c+1,i+1)
            )
            board[r][c] = temp
            return found
        
        for c in range(n):
            for r in range(m):
                if dfs(r,c,0):
                    return True
        return False
            

