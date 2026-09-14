class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # string version unbounded knapsack
        # dp[i] if s[:i] can be segmented
        # dp[i] = True if there is j < i s.t dp[j] == True and s[j:i] in wordSet
        wordSet = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[n]
