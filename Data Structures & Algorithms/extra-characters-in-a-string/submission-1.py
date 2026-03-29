class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        wordSet = set(dictionary)
        n = len(s)
        dp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            dp[i] = dp[i+1] + 1
            for j in range(i+1, n+1):
                word = s[i:j]
                if word in wordSet:
                    dp[i] = min(dp[i], dp[j])
        return dp[0]