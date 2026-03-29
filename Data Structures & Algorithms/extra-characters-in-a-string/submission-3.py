class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # === 1. Build Trie ===
        root = TrieNode()
        for word in dictionary:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.isWord = True

        n = len(s)
        dp = [0] * (n + 1)

        # base: no extra past the end
        dp[n] = 0

        # === 2. DP from right to left ===
        for i in range(n - 1, -1, -1):
            # Option 1: treat s[i] as an extra char
            dp[i] = dp[i + 1] + 1

            node = root
            # Try to match substrings s[i:j] using Trie
            for j in range(i, n):
                c = s[j]
                if c not in node.children:
                    break   # no longer matching any word
                node = node.children[c]
                if node.isWord:
                    dp[i] = min(dp[i], dp[j + 1])

        return dp[0]