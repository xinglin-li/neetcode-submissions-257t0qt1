class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        判断 word 是否能在 board 中通过一条由上下左右相邻单元格组成的路径被找到。
        同一个单元格在一次匹配里不可重复使用。

        Args:
            board: m x n 字符网格
            word: 目标字符串

        Returns:
            bool: 存在则 True，否则 False
        """
        m, n = len(board), len(board[0])

        def dfs(r: int, c: int, k: int) -> bool:
            """
            从坐标 (r, c) 开始，尝试匹配后缀 word[k:].

            参数:
                r: 当前行坐标，0 <= r < m
                c: 当前列坐标，0 <= c < n
                k: 目前已匹配前缀 word[:k]，此时必须让 board[r][c] == word[k]

            返回:
                若存在一条从 (r, c) 出发的路径能完成 word[k:], 返回 True；否则 False。
            """
            # 1) 全部匹配完成：k 走到了 len(word)
            if k == len(word):
                return True

            # 2) 越界或字符不等：此路不通
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            if board[r][c] != word[k]:
                return False

            # 3) 选择当前格子：(r,c) 作为 word[k]
            tmp = board[r][c]   # 备份
            board[r][c] = '#'   # 原地打标记，避免本轮重复使用

            # 4) 向四个方向递归匹配下一个字符 word[k+1]
            found = (
                dfs(r + 1, c, k + 1) or
                dfs(r - 1, c, k + 1) or
                dfs(r, c + 1, k + 1) or
                dfs(r, c - 1, k + 1)
            )

            # 5) 回溯：恢复现场，给其他分支用
            board[r][c] = tmp

            return found

        # 从每个起点 (i,j) 作为 word[0] 尝试：初始调用 dfs(i, j, 0)
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False



        