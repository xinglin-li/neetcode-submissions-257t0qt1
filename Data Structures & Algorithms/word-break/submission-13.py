class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        len_set = [len(w) for w in wordDict]
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1,n+1):
            for l in len_set:
                if l <= i and dp[i-l] and s[i-l:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]  
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]
"""
