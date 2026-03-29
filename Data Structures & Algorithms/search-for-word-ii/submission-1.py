class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class Node:
            def __init__(self):
                self.children = {}
                self.word = None
        
        root = Node()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = Node()
                node = node.children[ch]
            node.word = word
        
        m,n = len(board), len(board[0])
        ans = []
        def dfs(r,c,node):
            if r < 0 or r > m-1 or c <0 or c>n-1:
                return
            ch = board[r][c]
            if ch == "#":
                return
            if ch not in node.children:
                return

            nxt = node.children[ch]
            if nxt.word is not None:
                ans.append(nxt.word)
                nxt.word = None
            board[r][c] = "#"
            dfs(r-1,c,nxt)
            dfs(r,c-1,nxt)
            dfs(r+1,c,nxt)
            dfs(r,c+1,nxt)
            board[r][c] = ch

            if not nxt.children and nxt.word is None:
                node.children.pop(ch)

        for i in range(m):
            for j in range(n):
                dfs(i,j,root)
        return ans