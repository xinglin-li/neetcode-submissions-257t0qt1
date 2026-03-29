class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[n] = 1 (empty suffix), dp[n+1] conceptually 0 but we track with two vars
        next1, next2 = 1, 0  # next1 = dp[i+1], next2 = dp[i+2]
        
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                curr = 0
            else:
                # take one digit
                curr = next1
                # take two digits if valid 10..26
                if i + 1 < n and (1<=int(s[i:i+2])<=26):
                    curr += next2
            next1, next2 = curr, next1
        return next1



