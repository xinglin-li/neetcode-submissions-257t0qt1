class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # 1. construct Trie
        root = TrieNode()
        for word in dictionary:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.is_end = True
        
        n = len(s)
        # dp[i] 表示后缀 s[i:]（即从索引 i 到末尾）的最少额外字符数
        dp = [0] * (n + 1)

        # 2. 从后往前转移 DP 状态
        for i in range(n - 1, -1, -1):
            # 情况 1：假设 s[i] 是额外字符，多出 1 个字符
            dp[i] = dp[i+1] + 1
            # 情况 2：尝试从 s[i] 开始，沿着 Trie 前缀树匹配字典中的单词
            curr = root
            for j in range(i, n):
                char = s[j]
                if char not in curr.children:
                    break # 前缀树不存在该字符, 剪枝
                curr = curr.children[char]
                if curr.is_end:
                    dp[i] = min(dp[i], dp[j + 1])
        return dp[0]