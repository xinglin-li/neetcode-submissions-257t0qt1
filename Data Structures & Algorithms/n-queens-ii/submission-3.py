class Solution:
    def totalNQueens(self, n: int) -> int:
        # Optimized code using bitmask.
        def dfs(row, cols, diag1, diag2):
            if row == n:
                return 1
            count = 0
            # ((1<<4) - 1) -> 10000 - 1 -> 01111
            # available means take the last n digits of ~(cols|diag1|diag2)
            available = ((1<<n) - 1)& ~(cols|diag1|diag2)
            while available:
                # a + (-a) = 0. e.g. 0101 + 1011 -> 10000
                # There is a trick of complementary number.
                # a & (-a) will take the last non-zero digit
                pos = available & -available
                available -= pos
                count += dfs(
                    row + 1,
                    cols|pos,
                    # the mask of diag need to shift left or right by 1 digit.
                    # 1010 -> 0100, 1010 -> 0101
                    (diag1|pos) << 1,
                    (diag2|pos) >> 1
                )
            return count
        return dfs(0,0,0,0)