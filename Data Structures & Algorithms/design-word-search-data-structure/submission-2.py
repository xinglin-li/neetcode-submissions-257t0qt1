class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

    def search(self, word: str) -> bool:

        def dfs(i, node):
            # 走到结尾
            if i == len(word):
                return node.isWord

            c = word[i]

            # wildcard
            if c == '.':
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False

            # normal char
            if c not in node.children:
                return False

            return dfs(i + 1, node.children[c])

        return dfs(0, self.root)