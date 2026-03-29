class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # top-down + memo
        wordSet = set(dictionary)
        n = len(s)
        memo = {}

        def dfs(i):
            if i == n:
                return 0
            if i in memo:
                return memo[i]

            # 先假设 s[i] 这个字符是 extra
            ans = 1 + dfs(i + 1)

            # 枚举所有从 i 开始的子串
            for j in range(i, n):
                if s[i:j + 1] in wordSet:
                    ans = min(ans, dfs(j + 1))

            memo[i] = ans
            return ans

        return dfs(0)
            


            