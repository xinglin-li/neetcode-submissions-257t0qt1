class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.isWord = word
        
        res = []
        m, n = len(board), len(board[0])
        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            nxt = node.children[ch]
            if nxt.isWord is not None:
                res.append(nxt.isWord)
                nxt.isWord = None
            board[r][c] = "#"
            for dr, dc in [(1,0), (0, 1), (-1, 0), (0, -1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)
            board[r][c] = ch

        for r in range(m):
            for c in range(n):
                dfs(r,c,root)
        return res

