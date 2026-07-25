class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        wordSet = set(dictionary)
        n = len(s)
        dp = [0]*(n + 1) # dp[i] := # extras of s[i: n+1]

        for i in range(n-1, -1, -1):
            dp[i] = dp[i+1] + 1 # assume s[i] is extra first

            for j in range(i, n):
                if s[i:j+1] in dictionary:
                    dp[i] = min(dp[j+1], dp[i])
        
        return dp[0]