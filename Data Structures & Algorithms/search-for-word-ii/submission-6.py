class TrieNode:
    def __init__(self):
        self.words = dict()
        self.isWord = False

    def addWord(self, word):
        cur = self
        for i in word:
            if not cur.words.get(i):
                cur.words[i] = TrieNode()
            cur = cur.words[i]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        output = set()
        visited = set()

        def dfs(i, j, cur, string):
            if not (i >= 0 and j >= 0 and i < len(board) and j < len(board[0]) and (i,j) not in visited and board[i][j] in cur.words): # Exit condition
                return

            visited.add((i, j))
            string.append(board[i][j])
            cur = cur.words[board[i][j]]

            if cur.isWord: # Success condition
                output.add("".join(string))

            dfs(i-1, j, cur, string)
            dfs(i, j-1, cur, string)
            dfs(i+1, j, cur, string)
            dfs(i, j+1, cur, string)

            string.pop()
            visited.remove((i,j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root, [])
                
        return list(output)