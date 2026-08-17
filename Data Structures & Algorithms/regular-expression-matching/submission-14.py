class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j] 表示：s[i:] (s 从索引 i 到末尾的后缀) 能否与 p[j:] (p 从索引 j 到末尾的后缀) 匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # Base Case: 两个空后缀天然匹配 (s[m:] 与 p[n:] 均为 "")
        dp[m][n] = True
        # i 从 m 倒序到 0: 必须包含 i = m (即 s 为空后缀的情况，如 s="", p="a*b*")
        # j 从 n - 1 倒序到 0: p 为空且 s 非空时必定不匹配 (默认 False)
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                # 判断当前后缀的首字符是否匹配:
                # 1. 保证 s 尚未耗尽 (i < m)
                # 2. 当前字符相同，或者 p[j] 是通配符 '.'
                first_match = (i < m) and (p[j] == s[i] or p[j] == '.')
                # 情况一：p[j] 后面紧跟 '*' 修饰符，构成组合 token (如 "a*")
                if j + 1 < n and p[j + 1] == '*':
                    # 1. 匹配 0 次：直接跳过 "p[j]*"，转移到 dp[i][j + 2]
                    # 2. 匹配 1 次或多次：首字符必须匹配成功，消耗 s[i]，继续用 "p[j]*" 匹配 s 的下一个后缀 (dp[i + 1][j])
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])         
                # 情况二：普通单字符或 '.' (后面没有 '*')
                else:
                    # 首字符必须匹配，且两边各消耗一个字符，转移到下一个后缀
                    dp[i][j] = first_match and dp[i + 1][j + 1]                  
        # 返回完整字符串 s[0:] 与 p[0:] 的匹配结果
        return dp[0][0]