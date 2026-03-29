class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # O in the boarder is not considered to be surrounded
        m,n = len(board), len(board[0])
        connected = [[False]*n for _ in range(m)]
        def dfs(i,j, visited):

            if board[i][j] == 'X':
                return False
            
            if connected[i][j]:
                return True
            
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                connected[i][j] = True
                return True
            visited.add((i, j))
            dirs = [(1,0),(0,1),(-1,0),(0,-1)]
            for dx, dy in dirs:
                x, y = i+dx, j+dy
                if (x, y) not in visited:
                    if dfs(x, y, visited):
                        connected[i][j] = True
                        return True

            return False
        
        for i in range(m):
            for j in range(n):
                 if not dfs(i,j,set()):
                    board[i][j] = 'X'



        