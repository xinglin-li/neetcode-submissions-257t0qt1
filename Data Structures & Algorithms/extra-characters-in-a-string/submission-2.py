class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        wordSet = set(dictionary)
        n = len(s)
        
        dp = [0] * (n + 1)
        dp[n] = 0   # 从末尾开始
        
        for i in range(n - 1, -1, -1):
            # 1) 默认把 s[i] 当成 extra
            dp[i] = dp[i + 1] + 1
            
            # 2) 尝试匹配任意 s[i:j]
            for j in range(i + 1, n + 1):
                if s[i:j] in wordSet:
                    dp[i] = min(dp[i], dp[j])
        
        return dp[0]