class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = ways to decode of s[0:i]
        # if s[i-1] != 0: dp[i] += dp[i-1]
        # if 1 <= s[i-2:i] <= 26: dp[i] += dp[i-2]

        if not s or s[0] == "0":
            return 0
        
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1 # s[0:0]
        dp[1] = 1 # s[0:1]
        for i in range(2, n+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[n]