class PrefixTree:
    class Node:
        def __init__(self):
            # children: 当前节点的子节点映射，key=字符, value=下一个 Node
            self.children = {}
            # is_end: 该节点是否是某个单词的结尾
            self.is_end = False

    def __init__(self):
        # 初始化时建一个空的根节点
        self.root = PrefixTree.Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = PrefixTree.Node()
            node = node.children[ch]
        node.is_end = True   # 单词结束位置打标记

    def search(self, word: str) -> bool:
        """
        查找完整单词 word 是否在 Trie 中
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        判断是否存在任何插入的单词以 prefix 开头
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

        
        