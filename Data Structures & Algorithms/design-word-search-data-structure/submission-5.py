class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        """DFS 递归匹配，处理 '.' 通配符"""
        def dfs(start, node):
            curr = node
            for i in range(start, len(word)):
                char = word[i]
                # 遇到通配符 '.': 遍历当前节点的所有子分支
                if char == '.':
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                # 普通字符: 不存在则直接返回False
                if char not in curr.children:
                    return False
                curr = curr.children[char] # 指针移动是关键
            return curr.is_end
        return dfs(0, self.root)
        
