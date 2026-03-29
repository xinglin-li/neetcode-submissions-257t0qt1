class Solution:
    def countBits(self, n: int) -> List[int]:
        # i = (i>>1)*2 + 1&i
        # countBits(i) = countBits(i>>1) + (i&1)
        dp = [0]*(n+1)
        for i in range(1,n+1):
            dp[i] = dp[i>>1] + (i&1)
        return dp
"""
# naive approach
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ans.append(bin(i).count("1"))
        return ans
"""