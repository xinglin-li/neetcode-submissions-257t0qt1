class TrieNode:
    def __init__(self):
        self.children = {} # key为字符, value为对应的TrieNode节点
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """插入单词：逐字符向下延伸，不存在则新建节点"""
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        # 遍历结束后，将尾节点标记为单词结尾
        curr.is_end = True

    def search(self, word: str) -> bool:
        """精确查找：字符路径必须全部存在，且最后一个节点 is_end 为 True"""
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        """前缀查找：只要前缀路径完整存在即可，无需 is_end 为 True"""
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
        