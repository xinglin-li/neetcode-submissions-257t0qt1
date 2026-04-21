class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False]*n
        dp[0] = True
        pre = 0
        for i in range(1, n):
            if i - minJump >= 0:
                pre += dp[i-minJump]
            if i - maxJump > 0:
                pre -= dp[i-maxJump-1]
            dp[i] = (s[i] == "0" and pre > 0)
        return dp[-1]
