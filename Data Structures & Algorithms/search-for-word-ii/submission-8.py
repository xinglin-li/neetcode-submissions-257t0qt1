class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # directly save complete word, avoid retrospective search

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. construct Trie
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word
        
        m, n = len(board), len(board[0])
        res = []

        # 2. dfs backtrack
        def dfs(r, c, parent):
            char = board[r][c]
            curr_node = parent.children[char]
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None
            board[r][c] = "#"

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)
            
            board[r][c] = char

            if not curr_node.children:
                parent.children.pop(char)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] in root.children:
                    dfs(r,c,root)
        
        return res