class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        
        # col, diag1, diag2 are bitmasks
        def dfs(row, cols, diag1, diag2):
            if row == n:
                self.count += 1
                return
            
            # positions available at this row:
            # 1 bits means available columns
            available = (~(cols | diag1 | diag2)) & ((1 << n) - 1)
            
            while available:
                # pick the lowest '1' bit
                pos = available & -available
                available -= pos
                
                dfs(
                    row + 1,
                    cols | pos,
                    (diag1 | pos) << 1,
                    (diag2 | pos) >> 1
                )
        
        dfs(0, 0, 0, 0)
        return self.count