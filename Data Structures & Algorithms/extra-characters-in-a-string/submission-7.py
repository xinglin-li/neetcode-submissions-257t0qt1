class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        # 1. 构建字典的 Trie 树
        root = TrieNode()
        for word in dictionary:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.is_end = True

        n = len(s)
        # dp[i] 表示后缀 s[i:]（即从索引 i 到末尾）的最少额外字符数
        dp = [0] * (n + 1)

        # 2. 从后往前转移 DP 状态
        for i in range(n - 1, -1, -1):
            # 情况 1：假设 s[i] 是额外字符，多出 1 个字符
            dp[i] = dp[i + 1] + 1

            # 情况 2：尝试从 s[i] 开始，沿着 Trie 前缀树匹配字典中的单词
            curr = root
            for j in range(i, n):
                char = s[j]
                if char not in curr.children:
                    break  # 前缀树中不存在该字符，立刻剪枝中断
                curr = curr.children[char]
                if curr.is_end:
                    # 匹配到了合法单词 s[i:j+1]，更新 dp[i]
                    dp[i] = min(dp[i], dp[j + 1])

        return dp[0]