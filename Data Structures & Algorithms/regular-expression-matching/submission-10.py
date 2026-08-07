class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 定义 dp(i, j) 表示：字符串 s 从下标 i 开始的后缀，与模式串 p 从下标 j 开始的后缀是否能够匹配。
        from functools import cache

        @cache
        def dp(i, j):
            # Base Case：模式串 p 匹配完毕，必须 s 也刚好匹配完毕
            if j == len(p):
                return i == len(s)

            # 当前位置单字符是否匹配
            first_match = (i<len(s)) and (p[j] == s[i] or p[j] == '.')

            # 分情况处理 '*'
            if j + 1 < len(p) and p[j+1] == '*':
                # 匹配 0 次 OR 匹配 1 次以上
                return dp(i, j + 2) or (first_match and dp(i+1, j))
            else:
                # 普通单字符匹配
                return first_match and dp(i + 1, j + 1)
        
        return dp(0, 0)
