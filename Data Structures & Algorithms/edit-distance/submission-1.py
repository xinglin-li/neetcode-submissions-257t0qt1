class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # classical 2d dp
        # dp[i][j] -> minimum step to use word1[:i] to represent word2[:j]
        m, n = len(word1), len(word2)

        # dp[i][j] = min operations to convert word1[:i] → word2[:j]
        dp = [[0]*(n+1) for _ in range(m+1)]

        # Base cases
        for i in range(m+1):
            dp[i][0] = i      # delete i chars
        for j in range(n+1):
            dp[0][j] = j      # insert j chars

        # Fill dp table
        for i in range(1, m+1):
            for j in range(1, n+1):

                if word1[i-1] == word2[j-1]:
                    # Characters match → no new operation
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # A fact is that, in dp, all the operations are done for the last char
                    insert  = dp[i][j-1] + 1
                    delete  = dp[i-1][j] + 1
                    replace = dp[i-1][j-1] + 1

                    dp[i][j] = min(insert, delete, replace)

        return dp[m][n]
        
