class WordDictionary:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_end = False
    def __init__(self):
        self.root = WordDictionary.Node()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary.Node()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        # DFS：支持 '.' 的分支搜索
        def dfs(i: int, node: 'WordDictionary.Node') -> bool:
            if i == len(word):
                return node.is_end
            ch = word[i]

            if ch == '.':
                # '.' 可匹配任意一个字母：对所有孩子分支尝试
                for nxt in node.children.values():
                    if dfs(i + 1, nxt):
                        return True
                return False
            else:
                # 普通字符：走对应边
                if ch not in node.children:
                    return False
                return dfs(i + 1, node.children[ch])

        return dfs(0, self.root)


