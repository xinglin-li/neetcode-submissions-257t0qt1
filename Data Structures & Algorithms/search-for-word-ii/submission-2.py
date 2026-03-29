class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class Node:
            def __init__(self):
                self.children = {}
                self.word = None

        # build trie
        root = Node()
        for w in words:
            cur = root
            for ch in w:
                if ch not in cur.children:
                    cur.children[ch] = Node()
                cur = cur.children[ch]
            cur.word = w

        m, n = len(board), len(board[0])
        ans = []

        def dfs(r: int, c: int, node: Node):
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            ch = board[r][c]
            if ch == '#':
                return
            if ch not in node.children:
                return

            nxt = node.children[ch]          # 先走到下一个节点
            if nxt.word is not None:         # 再检查是否命中单词
                ans.append(nxt.word)
                nxt.word = None              # 防重复

            board[r][c] = '#'
            dfs(r+1, c, nxt)
            dfs(r-1, c, nxt)
            dfs(r, c+1, nxt)
            dfs(r, c-1, nxt)
            board[r][c] = ch

            # Trie 剪枝：该分支已无用则删除
            if not nxt.children and nxt.word is None:
                node.children.pop(ch)

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return ans
