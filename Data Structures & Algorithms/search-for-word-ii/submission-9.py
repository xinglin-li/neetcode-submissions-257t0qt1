class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # 记录完整单词, 方便直接获取

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. construct Trie
        root = TrieNode()
        for word in words:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.word = word
        
        rows, cols = len(board), len(board[0])
        res = []

        def backtrack(r: int, c: int, parent_node: TrieNode):
            char = board[r][c]
            curr_node = parent_node.children[char]

            # 命中一个完整单词
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None  # 避免同一单词被重复添加

            # 标记已访问（原地修改，避免开 visited 集合）
            board[r][c] = '#'

            # 上下左右四个方向扩散
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] in curr_node.children:
                        backtrack(nr, nc, curr_node)

            # 回溯恢复现场
            board[r][c] = char

            # 剪枝优化：如果当前节点没有子节点了，从父节点中删除它
            if not curr_node.children:
                parent_node.children.pop(char)

        # 遍历网格起点
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    backtrack(r, c, root)

        return res

